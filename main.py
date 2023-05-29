from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10)

        self.username_label = Label(text="Username:")
        layout.add_widget(self.username_label)
        self.username_input = TextInput(multiline=False)
        layout.add_widget(self.username_input)

        self.password_label = Label(text="Password:")
        layout.add_widget(self.password_label)
        self.password_input = TextInput(password=True, multiline=False)
        layout.add_widget(self.password_input)

        login_button = Button(text="Login")
        login_button.bind(on_press=self.login)
        layout.add_widget(login_button)

        self.add_widget(layout)

    def login(self, instance):
        # Add your login logic here
        username = self.username_input.text
        password = self.password_input.text
        # Implement your authentication logic

        print(f"Username: {username}")
        print(f"Password: {password}")


class SignUpScreen(Screen):
    def __init__(self, **kwargs):
        super(SignUpScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10)

        self.username_label = Label(text="Username:")
        layout.add_widget(self.username_label)
        self.username_input = TextInput(multiline=False)
        layout.add_widget(self.username_input)

        self.password_label = Label(text="Password:")
        layout.add_widget(self.password_label)
        self.password_input = TextInput(password=True, multiline=False)
        layout.add_widget(self.password_input)

        signup_button = Button(text="Sign Up")
        signup_button.bind(on_press=self.signup)
        layout.add_widget(signup_button)

        self.add_widget(layout)

    def signup(self, instance):
        # Add your sign-up logic here
        username = self.username_input.text
        password = self.password_input.text
        # Implement your sign-up logic

        print(f"Username: {username}")
        print(f"Password: {password}")


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        self.message_label = Label(text="Welcome to the Home Screen!")
        layout.add_widget(self.message_label)

        self.add_widget(layout)


class MyApp(App):
    def build(self):
        # Create the screen manager
        screen_manager = ScreenManager()

        # Create and add screens to the screen manager
        login_screen = LoginScreen(name="login")
        screen_manager.add_widget(login_screen)

        signup_screen = SignUpScreen(name="signup")
        screen_manager.add_widget(signup_screen)

        home_screen = HomeScreen(name="home")
        screen_manager.add_widget(home_screen)

        return screen_manager


if __name__ == '__main__':
    MyApp().run()
