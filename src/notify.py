from windows_toasts import Toast
from windows_toasts import ToastDisplayImage
from windows_toasts import WindowsToaster

from src.misc import resource_path

toaster = WindowsToaster("twentyx3")


def notify(text: str):
    toast = Toast()
    toast.text_fields = [text]
    toast.AddImage(ToastDisplayImage.fromPath(resource_path("src/assets/icon.png")))
    toaster.show_toast(toast)
