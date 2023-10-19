"""
Book tests.
"""

from lute.models.book import Book

def test_create_book(english):
    """
    When a book is created with given content, the content
    is split into separate Text objects.
    """
    fulltext = "Here is a dog. And a cat."
    scenario(english, fulltext, 5, ["Here is a dog.", "And a cat."], 7)
    scenario(english, fulltext, 500, ["Here is a dog. And a cat."], 7)
    scenario(english, fulltext + " And a thing.", 8,
             ["Here is a dog. And a cat.", "And a thing."], 10)
    scenario(english, "Here is a dog.\nAnd a cat.", 500, ["Here is a dog.\nAnd a cat."], 7)


def scenario(english, fulltext, maxwords, expected, expected_word_count):
    """
    Check scenarios.
    """
    b = Book.create_book('hi', english, fulltext, maxwords)

    actuals = [t.text for t in b.texts]
    print(actuals)
    assert "/".join(actuals) == "/".join(expected), f"scen {maxwords}"
    assert b.word_count == expected_word_count, "word count"


def test_smoke_datatables_query_runs(app_context):
    """
    Smoke test only, ensure query runs.
    """
    columns = [
        {
            "data": "0",
            "name": "BkID",
            "searchable": False,
            "orderable": False
        },
        {
            "data": "1",
            "name": "BkTitle",
            "searchable": True,
            "orderable": True
        },
    ]
    params = {
        "draw": "1",
        "columns": columns,
        "order": [
            {
                "column": "1",
                "dir": "asc"
            }
        ],
        "start": "10",
        "length": "50",
        "search": {
            "value": "",
            "regex": False
        }
    }

    d = Book.get_data_tables_list(params, False)
    print(d)
