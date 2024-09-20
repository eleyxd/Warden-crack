import requests

import time

from textual import on

from textual.app import App, ComposeResult

from textual.containers import Vertical, Horizontal, Container, ScrollableContainer

from textual.screen import Screen, ModalScreen

from textual.widgets import Button, Input, Label, Static



WKGPO3G = "ТОКЕН"

MIZ = 3

lrt = 0



def sb(term):

    global lrt

    current_time = time.time()

    if len(term) < MIZ:

        return "Минимальное количество для запроса 3 символа"

    if current_time - lrt < 30:

        return "Подождите 30 секунд перед запросом!"

    lrt = current_time

    url = "https://server.leakosint.com/"

    data = {

        "token": WKGPO3G,

        "request": term,

        "limit": 100,

        "lang": "ru"

    }

    try:

        response = requests.post(url, json=data)

        response.raise_for_status()

        results = response.json()

        if "List" not in results:

            return "Нет подключения к серверу!"

        output = []

        seen = set()

        for source, details in results["List"].items():

            if source == "Нет Результатов!":

                output.append("Информации не найдено")

                continue

            output.append(f"┍ {source}")

            for item in details.get("Data", []):

                item_str = str(item)

                if item_str in seen:

                    continue

                seen.add(item_str)

                max_key_length = max(len(key) for key in item.keys()) if item else 0

                for key, value in item.items():

                    output.append(f"│ {key:<{max_key_length + 3}} • {value.rstrip()}")

        if "Нет Результатов!" not in results["List"]:

            output.append("• • • • • • • •")

        return "\n".join(output)

    except requests.exceptions.RequestException:

        return "Ошибка при запросе к серверу"

    except Exception:

        return "• При повторном поиске, так-же ничего не найдено! "



class ResultScreen(ModalScreen[None]):

    

    def __init__(self, result_text: str = "", **kwargs):

        super().__init__(**kwargs)

        self.result_text = result_text



    def compose(self) -> ComposeResult:

        with Container(id="result-screen-container"):

            with ScrollableContainer():

                yield Label(self.result_text, id="result-label")

            yield Button("Exit", id="result-exit")



    def update_result(self, new_text: str):

        self.result_text = new_text

        self.query_one("#result-label", Label).update(new_text)



class Errors(ModalScreen[None]):



    def compose(self) -> ComposeResult:

        with Container(id="error-screen-container"):

            yield Label("Ожидайте, эта функция в разработке", id="result-label")

            yield Button("Exit", id="result-exit")



class WardenPageTwo(Screen):

    def compose(self) -> ComposeResult:

        with Vertical():

            with Horizontal(classes="button-container"):

                yield Button(label="Поиск по TIKTOK", id="tiktok_search")

                yield Button(label="Поиск по INSTAGRAM", id="instagram_search")

                yield Button(label="Поиск по MAC", id="mac_search")

                yield Button(label="Поиск по HWID", id="hwid_search")



            with Horizontal(classes="button-container"):

                yield Button(label="Поиск по USER-AGENT", id="user_agent_search")

                yield Button(label="Поиск по CARD", id="card_search")

                yield Button(label="Поиск по DOCUMENT", id="document_search")

                yield Button(label="Поиск по DATABASE", id="database_search")



            with Horizontal(classes="button-container"):

                yield Button(label="Поиск по DISCORD", id="discord_search")

                yield Button(label="Поиск по SIGNAL", id="signal_search")

                yield Button(label="Поиск по EMAIL", id="email_search")

                yield Button(label="Поиск по IMEI", id="imei_search")



            with Horizontal(classes="button-container"):

                yield Button("<<", id="zerotextbutton")

                yield Button(label="Поиск по GPS Cords", id="gps_cords_search")

                yield Button(label="Поиск по UDID", id="udid_search")

                yield Button(">>", id="threenextbutton")



            with Horizontal(classes="search-container"):

                yield Button(label="Искать", classes="search-button", variant="success", id="search_button")

                yield Input(placeholder="Введите запрос", classes="search-input", id="search_input")



class WardenPageThree(Screen):

    def compose(self) -> ComposeResult:

        with Vertical():

            with Horizontal(classes="button-container"):

                yield Button(label="Поиск по POLICY", id="policy_search")

                yield Button(label="Поиск по OSAGO", id="osago_search")

                yield Button(label="Поиск по CONTRACT", id="contract_search")

                yield Button(label="Поиск по LICENSE", id="license_search")



            with Horizontal(classes="button-container"):

                yield Button(label="Поиск по GIS", id="gis_search")

                yield Button(label="Поиск по GMP", id="gmp_search")

                yield Button(label="Поиск по EGRUL", id="egrul_search")

                yield Button(label="Поиск по EGRIP", id="egrip_search")



            with Horizontal(classes="button-container"):

                yield Button(label="Поиск по RDTS", id="rdts_search")

                yield Button(label="Поиск по VIN", id="vin_search")

                yield Button(label="Поиск по BASIC INFO", id="basic_info_search")

                yield Button(label="Поиск по RFID", id="rfid_search")



            with Horizontal(classes="button-container"):

                yield Button("<<", id="onetextbutton")

                #yield Button(label="Поиск по IMSI", id="imsi_search")

                yield Button(label="Поиск по OK", id="ok_search")

                yield Button(label="Поиск по IMSI", id="imsi_search")

                yield Button("Switch Style", id="switch_button")



            with Horizontal(classes="search-container"):

                yield Button(label="Искать", classes="search-button", variant="success", id="search_button")

                yield Input(placeholder="Введите запрос", classes="search-input", id="search_input")



class WardenPageOne(Screen):

    def compose(self) -> ComposeResult:

        with Vertical():

            with Horizontal(classes="button-container"):

                yield Button(label="Universal Search", id="universal_search")

                yield Button(label="Поиск по F.I.O", id="fio_search")

                yield Button(label="Поиск по NUMBER", id="number_search")

                yield Button(label="Поиск по WEBSITE", id="website_search")



            with Horizontal(classes="button-container"):

                yield Button(label="Поиск по DOMEN", id="domen_search")

                yield Button(label="Поиск по IP", id="ip_search")

                yield Button(label="Поиск по NICK", id="nick_search")

                yield Button(label="Поиск по LOGIN", id="login_search")



            with Horizontal(classes="button-container"):

                yield Button(label="Поиск по PASSWORD", id="password_search")

                yield Button(label="Поиск по INN", id="inn_search")

                yield Button(label="Поиск по SNILS", id="snils_search")

                yield Button(label="Поиск по PASSPORT", id="passport_search")



            with Horizontal(classes="button-container"):

                yield Button(label="Поиск по VK", id="vk_search")

                yield Button(label="Поиск по TELEGRAM", id="telegram_search")

                yield Button(label="Поиск по FACEBOOK", id="facebook_search")

                yield Button(">>", classes="next-page-button", id="onetextbutton")



            with Horizontal(classes="search-container"):

                yield Button(label="Искать", classes="search-button", variant="success", id="search_button")

                yield Input(placeholder="Введите запрос", classes="search-input", id="search_input")



class Warden(App[None]):

    CSS_PATH = "warden.tcss"

    SCREENS = {

        "a": WardenPageOne(),

        "b": WardenPageTwo(),

        "c": WardenPageThree(),

        "result": ResultScreen(),

        "error": Errors(),

    }



    async def on_mount(self):

        warden_art = """

            ▄█     █▄  

           ███     ███ 

           ███     ███

           ███     ███ 

           ███     ███ 

           ███     ███ 

           ███ ▄█▄ ███ 

            ▀███▀███▀  

        """



    def compose(self) -> ComposeResult:

        yield Button("Request", id="zerotextbuttons")

        yield Label(" ▄█     █▄", id="wardenonepart")

        yield Label("███     ███", id="wardentwopart")

        yield Label("███     ███", id="wardenthreepart")

        yield Label("███     ███", id="wardenfourpart")

        yield Label("███     ███", id="wardenfivepart")

        yield Label("███     ███", id="wardensixpart")

        yield Label("███ ▄█▄ ███", id="wardensevenpart")

        yield Label(" ▀███▀███▀", id="wardeneightpart")



    @on(Button.Pressed, "#zerotextbuttons")

    def pushss(self) -> None:

        self.push_screen("a")



    @on(Button.Pressed, "#switch_button")

    def error_text(self) -> None:

        self.push_screen("error")



    @on(Button.Pressed, "#zerotextbutton")

    def push(self) -> None:

        self.push_screen("a")



    @on(Button.Pressed, "#onetextbutton")

    def switch_to_two(self) -> None:

        self.switch_screen("b")



    @on(Button.Pressed, "#threenextbutton")

    def switch_to_three(self) -> None:

        self.switch_screen("c")



    @on(Button.Pressed, "#result-exit")

    def close_modal(self) -> None:

        self.app.pop_screen()



    @on(Input.Changed, "#search_input")

    def limit_input_digits(self, event):

        input_widget = event.input

        if input_widget.placeholder == "Введите номер (макс. 12 символов)":

            value = input_widget.value

            value = value.replace("+", "")

            value = '+' + ''.join(filter(str.isdigit, value))

            input_widget.value = value[:13]



    @on(Button.Pressed, "#number_search")

    def set_max_digits(self) -> None:

        input_widget = self.query_one("#search_input", Input)

        input_widget.value = ""

        input_widget.placeholder = "Введите номер (макс. 12 символов)"



    @on(Button.Pressed, "#universal_search")

    @on(Button.Pressed, "#fio_search")

    @on(Button.Pressed, "#domen_search")

    @on(Button.Pressed, "#ip_search")

    @on(Button.Pressed, "#nick_search")

    @on(Button.Pressed, "#login_search")

    @on(Button.Pressed, "#password_search")

    @on(Button.Pressed, "#inn_search")

    @on(Button.Pressed, "#snils_search")

    @on(Button.Pressed, "#passport_search")

    @on(Button.Pressed, "#vk_search")

    @on(Button.Pressed, "#telegram_search")

    @on(Button.Pressed, "#facebook_search")

    @on(Button.Pressed, "#tiktok_search")

    @on(Button.Pressed, "#instagram_search")

    @on(Button.Pressed, "#mac_search")

    @on(Button.Pressed, "#hwid_search")

    @on(Button.Pressed, "#user_agent_search")

    @on(Button.Pressed, "#card_search")

    @on(Button.Pressed, "#document_search")

    @on(Button.Pressed, "#database_search")

    @on(Button.Pressed, "#discord_search")

    @on(Button.Pressed, "#signal_search")

    @on(Button.Pressed, "#imei_search")

    @on(Button.Pressed, "#gps_cords_search")

    @on(Button.Pressed, "#udid_search")

    @on(Button.Pressed, "#policy_search")

    @on(Button.Pressed, "#osago_search")

    @on(Button.Pressed, "#contract_search")

    @on(Button.Pressed, "#license_search")

    @on(Button.Pressed, "#gis_search")

    @on(Button.Pressed, "#gmp_search")

    @on(Button.Pressed, "#egrul_search")

    @on(Button.Pressed, "#egrip_search")

    @on(Button.Pressed, "#rdts_search")

    @on(Button.Pressed, "#vin_search")

    @on(Button.Pressed, "#basic_info_search")

    @on(Button.Pressed, "#rfid_search")

    @on(Button.Pressed, "#imsi_search")

    @on(Button.Pressed, "#ok_search")

    @on(Button.Pressed, "#email_search")

    def reset_input_placeholder(self) -> None:

        input_widget = self.query_one("#search_input", Input)

        if input_widget:

            input_widget.value = ""

            input_widget.placeholder = "Введите запрос"



    @on(Button.Pressed, "#email_search")

    def set_email_input(self) -> None:

        input_widget = self.query_one("#search_input", Input)

        input_widget.value = ""

        input_widget.placeholder = "Введите Email"



    @on(Button.Pressed, "#search_button")

    def switch_to_result(self) -> None:

        input_widget = self.query_one("#search_input", Input)

        if input_widget.placeholder == "Введите Email" and "@" not in input_widget.value:

            terms = input_widget.value

            results = "Ошибка: Введите корректный Email, содержащий символ @"

            results_screen = ResultScreen(results)

            self.push_screen(results_screen)

        elif input_widget.placeholder == "Введите ссылку на Website" and "." not in input_widget.value:

            temss = input_widget.value

            resultss = "Ошибка: Введите корректную ссылку, содержащую ."

            resultss_screen = ResultScreen(resultss)

            self.push_screen(resultss_screen)

        else:

            input_widget = self.query_one(".search-input", Input)

            term = input_widget.value

            result = sb(term)

            result_screen = ResultScreen(result)

            self.push_screen(result_screen)



    @on(Button.Pressed, "#website_search")

    def set_website_input(self) -> None:

        input_widget = self.query_one("#search_input", Input)

        input_widget.value = ""

        input_widget.placeholder = "Введите ссылку на Website"



if __name__ == "__main__":

    Warden().run()
