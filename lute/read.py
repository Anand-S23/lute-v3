"""
/read endpoints.
"""

from flask import Blueprint, request, jsonify
from lute.utils.data_tables import DataTablesFlaskParamParser
from lute.models.book import Book

bp = Blueprint('read', __name__, url_prefix='/read')

@bp.route('/<int:bookid>/page/<int:pagenum>', methods=['GET'])
def read(bookid, pagenum):
    "Display reading pane for book page."
    return f"TODO book: reading book {bookid} page {pagenum}"
