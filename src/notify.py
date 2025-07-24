from windows_toasts import Toast
from windows_toasts import ToastDisplayImage
from windows_toasts import WindowsToaster

toaster = WindowsToaster("twentyx3")


def notify(text: str):
    toast = Toast()
    toast.text_fields = [text]
    toast.AddImage(ToastDisplayImage.fromPath("src/assets/icon.png"))
    toaster.show_toast(toast)
