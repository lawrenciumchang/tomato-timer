import rumps

class TomatoTimer(object):
  def __init__(self):
    self.config = {
      "app_name": "Tomato Timer",
      "start_25": "Start 25 Minute Timer",
      "start_10": "Start 10 Minute Timer",
      "start_5": "Start 5 Minute Timer",
      "pause": "Pause Timer",
      "continue": "Continue Timer",
      "stop": "Stop Timer",
      "break_message": "Time is up! Take a break! 😁",
      "25_min_interval": 1500,
      "10_min_interval": 600,
      "5_min_interval": 300
    }
    self.app = rumps.App(self.config['app_name'])
    self.timer = rumps.Timer(self.on_tick, 1)
    self.reset_menu()
    self.start_25_min_button = rumps.MenuItem(title=self.config['start_25'], callback=self.start_25)
    self.start_10_min_button = rumps.MenuItem(title=self.config['start_10'], callback=self.start_10)
    self.start_5_min_button = rumps.MenuItem(title=self.config['start_5'], callback=self.start_5)
    self.pause_button = rumps.MenuItem(title=self.config['pause'], callback=None)
    self.stop_button = rumps.MenuItem(title=self.config['stop'], callback=None)
    self.app.menu = [
      self.start_25_min_button,
      self.start_10_min_button,
      self.start_5_min_button,
      None, # Divider
      self.pause_button,
      self.stop_button, 
      None # Divider
    ]

  def reset_menu(self):
    self.timer.stop()
    self.timer.count = 0
    self.app.title = "🍅"

  def on_tick(self, sender):
    time_left = sender.end - sender.count
    mins = time_left // 60 if time_left >= 0 else time_left // 60 + 1
    secs = time_left % 60 if time_left >= 0 else (-1 * time_left) % 60
    if mins == 0 and time_left < 0:
      rumps.notification(title=self.config['app_name'], subtitle=self.config['break_message'], message='')
      self.reset_menu()
      self.stop_button.set_callback(None)
      self.reset_pause_continue_button()
      self.enable_all_start_timers()
    else:
      self.stop_button.set_callback(self.stop_timer)
      self.app.title = '🍅 ' + '{:2d}:{:02d}'.format(mins, secs)
    sender.count += 1

  #Enable all start timers
  def enable_all_start_timers(self):
    self.start_25_min_button.set_callback(self.start_25)
    self.start_10_min_button.set_callback(self.start_10)
    self.start_5_min_button.set_callback(self.start_5)

  # Disable all start timers
  def disable_all_start_timers(self):
    self.start_25_min_button.set_callback(None)
    self.start_10_min_button.set_callback(None)
    self.start_5_min_button.set_callback(None)

  # Enable pause/continue button
  def enable_pause_continue_button(self):
    self.pause_button.set_callback(self.pause_continue_timer)

  # Reset pause/continue button
  def reset_pause_continue_button(self):
    self.pause_button.title = self.config['pause']
    self.pause_button.set_callback(None)

  # Start 25 Minute Timer
  def start_25(self, sender):
    self.timer.count = 0
    self.timer.end = self.config['25_min_interval']
    self.disable_all_start_timers()
    self.enable_pause_continue_button()
    self.timer.start()

  # Start 10 Minute Timer
  def start_10(self, sender):
    self.timer.count = 0
    self.timer.end = self.config['10_min_interval']
    self.disable_all_start_timers()
    self.enable_pause_continue_button()
    self.timer.start()

  # Start 5 Minute Timer
  def start_5(self, sender):
    self.timer.count = 0
    self.timer.end = self.config['5_min_interval']
    self.disable_all_start_timers()
    self.enable_pause_continue_button()
    self.timer.start()

  # Pause / Continue Timer
  def pause_continue_timer(self, sender):
    # Continue
    if sender.title.lower().startswith('continue'):
      sender.title = self.config['pause']
      self.timer.start()
    # Pause
    else:
      sender.title = self.config['continue']
      self.timer.stop()

  # Stop Timer
  def stop_timer(self, sender):
    self.reset_menu()
    self.stop_button.set_callback(None)
    self.reset_pause_continue_button()
    self.enable_all_start_timers()

  def run(self):
    self.app.run()

if __name__ == '__main__':
  app = TomatoTimer()
  app.run()
