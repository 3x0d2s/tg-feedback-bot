from tgbot.handlers.common import register_handlers_common
from tgbot.handlers.new_ticket import register_handlers_new_ticket
from tgbot.handlers.dialogs.create_dialog import register_handlers_create_dialog
from tgbot.handlers.dialogs.dialog_router import register_handlers_dialog_router


def register_handlers(dp):
    register_handlers_dialog_router(dp)
    register_handlers_common(dp)
    register_handlers_new_ticket(dp)
    register_handlers_create_dialog(dp)
