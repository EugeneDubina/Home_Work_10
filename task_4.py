for elements in ['разработка', 'администрирование', 'protocol', 'standard']:
    a = elements.encode('utf-8', 'replace')
    b = a.decode('utf-8')
    print(elements, a, b)