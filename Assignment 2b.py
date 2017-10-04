# Created by: Scarlett Gao
# Created on: 2-Oct-2017
# Created for: ICS3U

import ui

def calculate_button_touch_up_inside(sender):
	  # calculate circumference
	  
# constant
  g = 9.81
  
# input
  second = int(view['second_textbox'].text)
  
# process
  height = 100.0 - ((0.5) * g * second ** 2)
  
# output
  view['height_label'].text = 'The Height is : ' + str(height)
  
view = ui.load_view()
view.present('full_screen')
