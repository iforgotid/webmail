import mandrill
mandrill_client = mandrill.Mandrill('kSeK7plXVJ0b2JuCfSLJ5A')
message = {
    'from_email': 'philipp.xue@gmail.com',
    'from_name': 'Xue Jiaqi',
    'html': '<p>Example HTML content</p>',
    'important': False,
    'subject': 'example subject',
    'text': 'Example text content',
    'to': [{'email': 'philipp.xue@gmail.com',
            'name': 'Xue Jiaqi',
            'type': 'to'}],
}
result = mandrill_client.messages.send(message=message, async=False)
