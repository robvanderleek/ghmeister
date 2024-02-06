from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, ListView, ListItem, Label

from repomeister.services.GitHubService import get_github


class RepoMeisterApp(App):
    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header()
        list_view = ListView()
        for r in get_github().get_user().get_repos(affiliation='owner'):
            list_item = ListItem(Label(r.full_name), name=r.full_name)
            list_view.append(list_item)
        yield list_view
        yield Footer()

    def action_quit(self) -> None:
        self.exit()
