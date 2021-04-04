


def words_number(words):
    starts_numeric = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
    count_hundred= 1000
    count_thousand = count_hundred * 1000
    count_million = count_thousand * 1000
    count_billion = count_million * 1000

    assert(0 <= words)

    if (words < 20):
        return starts_numeric[words]

    if (words < 100):
        if words % 10 == 0: 
            return starts_numeric[words]
        else: 
            return starts_numeric[words // 10 * 10] + '-' + starts_numeric[words % 10]

    if (words < count_hundred):
        if words % 100 == 0: 
            return starts_numeric[words // 100] + ' hundred'

        else: 
            return starts_numeric[words // 100] + ' hundred and ' + words_number(words % 100)

    if (words < count_thousand):
        if words % count_hundred == 0: 
            return words_number(words // count_hundred) + ' thousand'
        else: 
            return words_number(words // count_hundred) + ' thousand, ' + words_number(words % count_hundred)

    if (words < count_million):
        if (words % count_thousand) == 0: 
            return words_number(words // count_thousand) + ' million'
        else: 
            return words_number(words // count_thousand) + ' million, ' + words_number(words % count_thousand)

    if (words < count_billion):       
        if (words % count_million) == 0: 
            return words_number(words // count_million) + ' billion'
        else: 
            return words_number(words // count_million) + ' billion, ' + words_number(words % count_million)

    if (words % count_billion == 0): 
        return words_number(words // count_billion) + ' trillion'
    else: 
        return words_number(words// count_billion) + ' trillion, ' + words_number(words % count_billion)

    raise AssertionError('words is too large: %s' % str(words))

print(words_number(1208))