from app.ask import describe_usage_metadata


class DummyUsage:
    prompt_token_count = 123
    candidates_token_count = 45


class DummyResponse:
    usage_metadata = DummyUsage()


def test_describe_usage_metadata_formats_token_counts():
    assert describe_usage_metadata(DummyResponse()) == "入力トークン数: 123 / 出力トークン数: 45"
