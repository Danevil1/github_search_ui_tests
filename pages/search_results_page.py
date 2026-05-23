"""GitHub search results page object."""

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from pages.base_page import BasePage
from pages.repository_page import RepositoryPage


class SearchResultsPage(BasePage):
    """Page Object for GitHub search results."""

    REPOSITORIES_TAB_XPATH = (
        "//a["
        "contains(@href, 'type=repositories') "
        "and (contains(normalize-space(.), 'Repositories') "
        "or contains(normalize-space(.), 'repositories'))"
        "]"
    )

    COPILOTKIT_REPOSITORY_LINK_XPATH = (
        "//a["
        "contains(@href, '/CopilotKit/CopilotKit') "
        "and (contains(normalize-space(.), 'CopilotKit') "
        "or contains(@href, 'CopilotKit'))"
        "]"
    )

    GENERIC_REPOSITORY_LINK_XPATH_TEMPLATE = (
        "//a["
        "contains(@href, '/{repo_name}') "
        "and contains(translate(normalize-space(.), "
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "
        "'abcdefghijklmnopqrstuvwxyz'), '{repo_name_lower}')"
        "]"
    )

    def open_repository_by_name(self, repo_name: str) -> RepositoryPage:
        """Open target repository from search results."""
        self._open_repositories_tab_if_available()

        if repo_name.lower() == "copilotkit":
            repository_link = self.first_visible_xpath(
                self.COPILOTKIT_REPOSITORY_LINK_XPATH
            )
        else:
            repository_link = self.first_visible_xpath(
                self.GENERIC_REPOSITORY_LINK_XPATH_TEMPLATE.format(
                    repo_name=repo_name,
                    repo_name_lower=repo_name.lower(),
                )
            )

        repository_link.click()
        self.page.wait_for_load_state("domcontentloaded")
        return RepositoryPage(self.page)

    def _open_repositories_tab_if_available(self) -> None:
        """Switch search results to repositories if the tab is present."""
        repositories_tab = self.xpath(self.REPOSITORIES_TAB_XPATH).first

        try:
            repositories_tab.wait_for(state="visible", timeout=5_000)
            repositories_tab.click()
            self.page.wait_for_load_state("domcontentloaded")
        except PlaywrightTimeoutError:
            # The global search can already be opened in repository results.
            return
