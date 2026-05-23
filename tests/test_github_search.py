"""UI tests for GitHub global search."""

from playwright.sync_api import Page

from pages.github_home_page import GitHubHomePage


def test_user_can_find_copilotkit_repository_from_global_search(
    page: Page,
) -> None:
    """Search for 'copilot', open CopilotKit repo and verify README text."""
    home_page = GitHubHomePage(page)

    home_page.open()
    search_results_page = home_page.search_for("copilot")
    repository_page = search_results_page.open_repository_by_name("CopilotKit")

    repository_page.should_be_opened("CopilotKit", "CopilotKit")
    repository_page.should_contain_readme_text("CopilotKit")
