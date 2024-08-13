import pandas as pd
from utils import get_words


class InvertedIndex:
    def __init__(self) -> None:
        # Maps unique words to document_id and tf score.
        # unique_words -> (doc_id, tf_score).
        self.inverted_lists_: dict[str, list[int]] = {}
        # self.inverted_lists_: dict[str, list[tuple[int, int]]] = {}

        # Store document_ids.
        self.doc_ids_: list[int] = []

        self.movies_: list[tuple[str, str]] = []

    def build_from_file(self, file_name: str) -> None:
        # Interprete each line as a document.
        df = pd.read_csv(file_name)
        doc_id: int = 1
        for _, row in df.iterrows():
            row_data = {'title': row['title'],
                        'date_x': row['date_x'],
                        'score': row['score'], 
                        'genre': row['genre'], 
                        'overview': row['overview'],
                        'crew': row['crew']
                        }
            title, date, score, genre ,overview, crew = get_words(row_data['title']), row_data['date_x'], row_data['score'], get_words(row_data['genre']) ,get_words(row_data['overview']), get_words(row_data['crew'])
            for word in title + overview + genre + crew:
                if word not in self.inverted_lists_:
                    self.inverted_lists_[word] = [doc_id]
                else:
                    if self.inverted_lists_[word][-1] != doc_id:
                        self.inverted_lists_[word].append(doc_id)
            self.doc_ids_.append(doc_id)
            self.movies_.append((row['title'], row['overview']))
            doc_id += 1

    def intersect(self, array1: list[int], array2: list[int]) -> list[int]:
        i, j = 0, 0
        n, m = len(array1), len(array2)
        result: list[int] = []
        while i < n and j < m:
            if array1[i] == array2[j]:
                result.append(array1[i])
                i += 1
                j += 1
            elif array1[i] < array2[j]:
                i += 1
            elif array1[i] > array2[j]:
                j += 1
        return result

    def prozess_query(self, query_words: list[str]) -> list[int]:
        if len(query_words) == 0:
            return []
        result: list[int] = []
        for index, word in enumerate(query_words):
            if word in self.inverted_lists_: 
                result = self.inverted_lists_[word]
                query_words = query_words[index:]
                break
        for word in query_words:
            if word in self.inverted_lists_: 
                result = self.intersect(result, self.inverted_lists_[word])
        return result

    def generate_output(self, query: str, threshold: int = 15) -> None:
        query_words: list[str] = get_words(query)
        query_result = self.prozess_query(query_words)
        print(f"Query: {query}")
        if len(query_result) == 0:
            return
        for i, index in enumerate(query_result):
            print(f"{self.movies_[index-1][0]}")
            if i > 15:
                break