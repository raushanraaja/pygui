import dearpygui.dearpygui as dpg
from threading import Thread
from time import sleep



def get_values():
    import random
    import string
    return [''.join(random.choices(string.ascii_uppercase + string.digits, k=30)) for _ in range(3)]


def update_inputs():
    while True:
        values = get_values()
        current_input_one = dpg.get_value("input#01")
        current_input_two = dpg.get_value("input#02")
        current_input_three = dpg.get_value("input#03")
        dpg.set_value("input#01", current_input_one + "\n" + values[0])
        dpg.set_value("input#02", current_input_two + "\n" + values[1])
        dpg.set_value("input#03", current_input_three + "\n" + values[2])
        sleep(0.5)


def run():
    Thread(target=update_inputs, daemon=True).start()


dpg.create_context()
with dpg.font_registry():
    dpg.add_font("assets\\fonts\\RobotoMono-Italic-VariableFont_wght.ttf", 20, tag="roboto-italic", default_font=True)
    dpg.add_font("assets\\fonts\\RobotoMono-VariableFont_wght.ttf", 20, tag="roboto", default_font=True)

dpg.bind_font("roboto")
dpg.set_global_font_scale(1)

with dpg.window(no_title_bar=True, no_close=True, no_collapse=True, no_resize=True, no_move=True, no_background=True,  pos=[0, 0], width=1400, height=520, ):
    with dpg.group(horizontal=True):
        with dpg.group(width=450, height=400):
            dpg.add_text("Label 1")
            dpg.add_input_text(multiline=True, enabled=False, tag="input#01", track_offset=1, tracked=True)
        with dpg.group(width=450, height= 400):
            dpg.add_text("Label 2")
            dpg.add_input_text(multiline=True, enabled=False, tag="input#02", tracked=True)
        with dpg.group(width=450, height= 400):
            dpg.add_text("Label 3")
            dpg.add_input_text(multiline=True, enabled=False, tag="input#03", tracked=True)

    dpg.add_button(label="Start", callback=run)


dpg.create_viewport(title='Custom Title',width=1400 , height=520)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()