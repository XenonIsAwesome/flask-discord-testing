from bot.custom_modal_submits.translate_modal_submit import TranslateModalSubmit

def ModalSubmitFactory():
    modal_submits = {
        TranslateModalSubmit.custom_id: TranslateModalSubmit()
    }