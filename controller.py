import view
import logger
import model

def start():
    while True:
        mode = view.choose_mode()
        if mode == '1':
            contact = view.new_contact()
            logger.add_new(contact)
        elif mode == '2':
            contact = view.search_inf()
            base = logger.get_base()
            result = model.search_contact(base, contact)
            view.show_found(result)
        elif mode == '3':
            base = logger.get_base()
            print(base)
        elif mode == '4':
            return False
