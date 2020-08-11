import xml.etree.cElementTree as ET

def post_mfd_parameter(event, key):
    """Return a key/value pair from a POST body multipart/form-data"""
    data = parse_multipart_form_data(event)
    return data[key]

def parse_multipart_form_data(event):
    """Parse Content-Type: multipart/form-data
    This is a quickly-made parser, and in the future should be replaced
    with a 3rd party library.
    """
    # Confirm Content-Type
    if event['headers']['Content-Type'][0:19] != 'multipart/form-data':
        return

    # Parse the multipart form-data (very annoying)
    body = event['body']
    data = {}
    i = 1
    n_parameters = body.count('\r\n\r\n')
    for p in range(n_parameters):
        # Algorithm:
        # find \r\n--
        #     from \r\nContent-Disposition: form-data; name=\"
        #     to \"
        # find \r\n\r\n
        #     from \r\n\r\n
        #     to \r\n--

        txt = '\r\nContent-Disposition: form-data; name=\"'
        i = body.find(txt, i+1)
        i += len(txt)
        k_start = i

        txt = '\"\r\n'
        i = body.find(txt, i+1)
        k_end = i
        i += len(txt)
    
        txt = '\r\n\r\n'
        i = body.find(txt, i+1)
        i += len(txt)
        v_start = i

        txt = '\r\n'
        i = body.find(txt, i+1)
        v_end = i
        i += len(txt)

        key = body[k_start:k_end]
        value = body[v_start:v_end]
    
        data[key] = value

    return data

def xml_serialize(data, root):
    """Return xml from data in dictionary
    This is a rought version, should be replace with proper libraries"""
    xt = ET.Element(root)
    for key, value in data.items():
        value_str = str(value)
        if value_str == '':
           value_str = ' '  # cheesy way to prevent empty tags </likethis>
        ET.SubElement(xt, key).text = value_str
    xmlstr = ET.tostring(xt, encoding='utf8', method='xml').decode()
    xmlstr = xmlstr.replace('> </', '></')
    xmlstr = xmlstr.replace('\n', '')  # prevent empty tags, part 2
    return xmlstr
