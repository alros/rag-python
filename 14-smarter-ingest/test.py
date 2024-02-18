from PDFDirectoryReader import HeaderCleansing


def test(input, prev, expected):
    header = HeaderCleansing().cleanse(input, prev)
    assert header == expected
    return header


header = test('', '', '')
header = test('Dementia > Contents > 1.1 Disease – 2 > 1.1.4 Prognosis – 12', header, '1.1 Disease > 1.1.4 Prognosis')
header = test('Dementia > Contents > 1.1 Disease – 2 > 1.1.4 Prognosis – 12 > 1.1 Disease', header,
              '1.1 Disease > 1.1.4 Prognosis')
header = test('Dementia > Contents > 1.1 Disease – 2 > 1.1.4 Prognosis – 12 > 1.1 Disease > Definition > Dementia',
              header, '1.1 Disease > 1.1.4 Prognosis')
header = test('Dementia > 1.1.1 Forms of Dementia', header, '1.1 Disease > 1.1.1 Forms of Dementia')
header = test('Dementia > 1.1.1 Forms of Dementia > . Fig. 1.1 Alois Alzheimer', header,
              '1.1 Disease > 1.1.1 Forms of Dementia')

#

header = test('Dementia > 1.1.1 Forms of Dementia > . Fig. 1.1 Alois Alzheimer',
              '1.1 Disease > 1.1.1 Forms of Dementia', '1.1 Disease > 1.1.1 Forms of Dementia')
header = test('Dementia > Risk factors for vascular dementia',
              '1.1 Disease > 1.1.1 Forms of Dementia', '1.1 Disease > 1.1.1 Forms of Dementia')

print('all ok!')
