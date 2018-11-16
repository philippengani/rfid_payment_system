import lcddriver

lcd = lcddriver.lcd()

def display(message,position):
    lcd.lcd_display_string(str(message),position)

    
    
    
