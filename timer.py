import tkinter as tk
import pydub.audio_segment as audio
import pydub.playback
import queue
import threading
import time


class PlaybackHelper(threading.Thread):
    def __init__(self, queue):
        super().__init__(group=None, target=self)

        self._queue = queue
        self._sound = audio.AudioSegment.from_mp3('sounds/classic_alarm.mp3')

    def _alive(self):
        try:
            _ = self._queue.get(block=False)
        except queue.Empty:
            return True

        return False

    def run(self):
        while self._alive():
            pydub.playback.play(self._sound[:1000])
            time.sleep(0.500)


class Timer(tk.Frame):
    STATE_STOPPED = 0
    STATE_PAUSE = 1
    STATE_RUNNING = 2

    def __init__(self, root=tk.Tk()):
        super().__init__(root)

        self._root = root
        self._state = Timer.STATE_STOPPED
        self._seconds = 0
        self._queue = queue.Queue()

        self.pack()
        self._create_elements()

    def _create_elements(self):

        self._fr_controls = tk.Frame(self)

        #labels
        self._lbl_hours = tk.Label(self, text="00")
        self._lbl_minutes = tk.Label(self, text="00")
        self._lbl_seconds = tk.Label(self, text="00")
        self._lbl_timer = tk.Label(self, text="hh:mm:ss")

        #buttons
        self._bttn_hours_up = tk.Button(self, text="\u25B2")
        self._bttn_hours_down = tk.Button(self, text="\u25BC")
        self._bttn_minutes_up = tk.Button(self, text="\u25B2")
        self._bttn_minutes_down = tk.Button(self, text="\u25BC")
        self._bttn_seconds_up = tk.Button(self, text="\u25B2")
        self._bttn_seconds_down = tk.Button(self, text="\u25BC")

        self._bttn_start = tk.Button(self._fr_controls, text="start")
        self._bttn_stop = tk.Button(self._fr_controls, text="stop")
        self._bttn_pause = tk.Button(self._fr_controls, text="pause")
        self._bttn_clear = tk.Button(self._fr_controls, text="clear")

        #event handler
        self._bttn_hours_up['command'] = lambda : \
            self._update_time_labels(self._lbl_hours, 1)
        self._bttn_hours_down['command'] = lambda : \
            self._update_time_labels(self._lbl_hours, -1)
        self._bttn_minutes_up['command'] = lambda : \
            self._update_time_labels(self._lbl_minutes, 1)
        self._bttn_minutes_down['command'] = lambda : \
            self._update_time_labels(self._lbl_minutes, -1)
        self._bttn_seconds_up['command'] = lambda : \
            self._update_time_labels(self._lbl_seconds, 1)
        self._bttn_seconds_down['command'] = lambda : \
            self._update_time_labels(self._lbl_seconds, -1)

        self._bttn_start['command'] = self._start
        self._bttn_stop['command'] = self._stop
        self._bttn_pause['command'] = self._pause
        self._bttn_clear['command'] = self._clear


        #layout
        self._lbl_hours.grid(row=0, column=0, rowspan=2)
        self._lbl_minutes.grid(row=0, column=2, rowspan=2)
        self._lbl_seconds.grid(row=0, column=4, rowspan=2)
        self._lbl_timer.grid(row=2, column=0, columnspan=6)
        self._bttn_hours_up.grid(row=0, column=1)
        self._bttn_hours_down.grid(row=1, column=1)
        self._bttn_minutes_up.grid(row=0, column=3)
        self._bttn_minutes_down.grid(row=1, column=3)
        self._bttn_seconds_up.grid(row=0, column=5)
        self._bttn_seconds_down.grid(row=1, column=5)

        self._bttn_start.grid(row=0, column=0) 
        self._bttn_stop.grid(row=0, column=1)
        self._bttn_pause.grid(row=0, column=2)
        self._bttn_clear.grid(row=0, column=3)

        self._fr_controls.grid(row=3, column=0, columnspan=6)
    
    def _update_time_labels(self, elem, incr):
        new_value = int(elem.cget('text')) + incr
        if new_value >= 0:
            elem['text'] = '{:02d}'.format(new_value)

    def _format_seconds(self, seconds):
        h = seconds // 3600
        m = seconds % 3600 // 60
        s = seconds % 60

        return '{:02d}:{:02d}:{:02d}'.format(h, m, s)

    def _start(self):
        self._seconds = int(self._lbl_hours.cget('text')) * 3600 +\
                        int(self._lbl_minutes.cget('text')) * 60 +\
                        int(self._lbl_seconds.cget('text'))
        self._lbl_timer['text'] = self._format_seconds(self._seconds)

        self._state = Timer.STATE_RUNNING
        self._root.after(1000, self._run)

    def _stop(self):
        self._state = Timer.STATE_STOPPED

        if self._seconds == 0:
            self._queue.put(0)
            
    def _pause(self):
        if self._state == Timer.STATE_RUNNING:
            self._state = Timer.STATE_PAUSE
        elif self._state == Timer.STATE_PAUSE:
            self._state = Timer.STATE_RUNNING
            self._root.after(1000, self._run)

    def _clear(self):
        self._lbl_hours['text'] = '00'
        self._lbl_minutes['text'] = '00'
        self._lbl_seconds['text'] = '00'
        self._lbl_timer['text'] = 'hh:mm:ss'


    def _run(self):
        if self._state == Timer.STATE_RUNNING:
            if self._seconds -1 >= 0:
                self._seconds -= 1
                self._lbl_timer['text'] = self._format_seconds(self._seconds)
            if self._seconds >0:
                self._root.after(1000, self._run)
            else:
                PlaybackHelper(self._queue).start()
                

if __name__ == '__main__':
    Timer().mainloop()  