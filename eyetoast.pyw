from win10toast import ToastNotifier
import time

def notify():
	toaster = ToastNotifier()                        
	toaster.show_toast("Take a break for your eyes",
			   '20-20-20 Rule',
			    icon_path=None,
			    duration=7)
	while toaster.notification_active(): time.sleep(0.1)

if __name__ == "__main__":
        notify()
		
