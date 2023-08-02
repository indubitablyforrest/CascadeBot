import cascade


def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == '/cascade':
        return cascade.cascade_resolved()

    if p_message == '/help' | '/commands':
        return 'here is what i can do: /cascade, /help'
