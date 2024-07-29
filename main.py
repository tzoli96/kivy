# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget

class GraphWidget(Widget):
    def __init__(self, **kwargs):
        super(GraphWidget, self).__init__(**kwargs)
        self.data = {'victories': [], 'defeats': [], 'touches_scored': [], 'touches_received': []}
        self.max_value = 350

    def update_graph(self, category, value):
        self.data[category].append(value)
        self.draw_graph()

    def draw_graph(self):
        self.canvas.clear()
        categories = list(self.data.keys())
        with self.canvas:
            for i, category in enumerate(categories):
                if category == 'defeats':
                    Color(1, 0, 0)
                elif category == 'victories':
                    Color(0, 0, 1)
                elif category == 'touches_scored':
                    Color(1, 0.5, 0)
                elif category == 'touches_received':
                    Color(1, 0, 1)
                x = 50 + i * 100
                for j, value in enumerate(self.data[category]):
                    height = (value / self.max_value) * 300
                    y = 50
                    Rectangle(pos=(x + j * 20, y), size=(15, height))

class PerformanceApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')

        # Top section for Month and Season
        top_section = GridLayout(cols=2, size_hint=(1, 0.1))
        top_section.add_widget(Label(text='Month:'))
        top_section.add_widget(Label(text='September'))
        top_section.add_widget(Label(text='Season:'))
        top_section.add_widget(Label(text='2024-2025'))

        # Middle section for Weekly Results
        middle_section = GridLayout(cols=4, size_hint=(1, 0.2))
        categories = ['Victories', 'Defeats', 'Touches Scored', 'Touches Received']
        for category in categories:
            category_layout = BoxLayout(orientation='vertical')
            category_layout.add_widget(Label(text=category))
            for i in range(4):
                btn = Button(text=str(i + 1))
                btn.bind(on_release=lambda instance, cat=category.lower().replace(' ', '_'), value=(i + 1) * 10: self.update_results(cat, value))
                category_layout.add_widget(btn)
            middle_section.add_widget(category_layout)

        # Bottom section for Graph
        self.graph = GraphWidget(size_hint=(1, 0.7))

        # Add sections to the root layout
        root.add_widget(top_section)
        root.add_widget(middle_section)
        root.add_widget(self.graph)

        return root

    def update_results(self, category, value):
        self.graph.update_graph(category, value)

if __name__ == '__main__':
    PerformanceApp().run()
