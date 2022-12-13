from datetime import datetime


def paint(obiekt_funkcyjny):
    def opakowanie():
        przed_wywolaniem = datetime.now()
        obiekt_funkcyjny()
        po_wywolaniu = datetime.now()
        print(f'wywloanie zajelo mi: {po_wywolaniu - przed_wywolaniem}')

    return opakowanie


@paint
def cos_robie():
    a = [x for x in range(50000)]


@paint
def jednak_nic_nie_robie():
    print('lazy')


cos_robie()
jednak_nic_nie_robie()