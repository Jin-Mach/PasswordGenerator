from src.ui.dialog.dialog_manager import DialogManager
from src.utilities.logging_manager import get_logger


class ExceptionManager:

    @staticmethod
    def exception_handler(exception: Exception, parent=None) -> None:
        logger = get_logger()
        logger.error("An error occurred: %s", exception, exc_info=True)
        DialogManager.show_error_message(exception, parent)