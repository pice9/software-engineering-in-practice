from notifier.notifier import InMemoryNotifier, send_receipt_ready, SilentNotifier


def test_send_receipt_ready_notifies_with_order_id():
    notifier = InMemoryNotifier()

    send_receipt_ready(notifier, "A123")

    assert notifier.sent_messages == ["Order A123 is ready."]


def test_send_silent_notifier_returns_nothing():
    notifier = SilentNotifier

    send_receipt_ready(notifier, "A123")