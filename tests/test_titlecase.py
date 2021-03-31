from titlecase import title_case


class TitleCassTests:

    # Given lowercase text and returned text should be uppercased correctly
    def test_lower_text_is_uppercased_correctly(self):
        initial_text = 'this should be capitalized'
        expected_text = 'This Should Be Capitalized'
        returned_text = title_case(initial_text)
        assert returned_text == expected_text
