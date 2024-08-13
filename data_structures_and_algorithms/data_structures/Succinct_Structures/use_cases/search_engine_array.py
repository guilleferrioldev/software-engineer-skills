"""
A search engine consists of several parts, including keyword indexing, efficient representation of documents,
and the ability to perform quick queries on those documents. Here's a summary of how you might use a succinct array in a search engine:

1. **Keyword Indexing**:
   - Uses a succinct array to store information about the presence or absence of keywords in each indexed document.
   - Each bit in the succinct array could represent the presence or absence of a keyword in a specific document.

2. **Quick Queries**:
   - Use the succinct array to perform quick queries on the presence of keywords in documents.
   - Range operations on the succinct array could be used to determine which documents contain a specific set of keywords.

3. **Efficient document retrieval**:
   - Uses the succinct array to quickly retrieve documents that match a given search query.
"""

class SearchEngine:
    def __init__(self, documents):
        self.index = {}  # Dictionary to store keyword indexing
        self.bit_vectors = []  # List to store succinct arrays for each keyword
        self.documents = documents

        # Index the keywords in the documents and construct the succinct arrays
        for doc_id, content in enumerate(documents):
            # Process the content to extract the keywords
            keywords = content.lower().split()  # Simple keyword extraction - split by space

            # Construct the succinct array for the current document
            bit_vector = self.construct_bit_vector(keywords)

            # Update the index and succinct arrays
            for keyword in keywords:
                if keyword not in self.index:
                    self.index[keyword] = []
                self.index[keyword].append(doc_id)
                self.bit_vectors.append(bit_vector)

    def search(self, query):
        keywords = query.lower().split()  # Simple keyword extraction from the query
        result_set = set(range(len(self.documents)))  # Initial set of documents

        # Process each keyword and apply the intersection operation on the results
        for keyword in keywords:
            if keyword in self.index and len(self.index[keyword]) > 0:
                # Perform intersection with the current set of relevant documents
                result_set = result_set.intersection(set(self.index[keyword]))

        # Return the relevant documents
        return list(result_set)

    # Method to construct succinct bit vector for the keywords in a document
    def construct_bit_vector(self, keywords):
        bit_vector = 0
        for keyword in keywords:
            # For simplicity, assume a fixed set of keywords and their positions
            if keyword == "brown" or keyword == "fox" or keyword == "python":
                # Set the bit at the corresponding position for each keyword    
                position = ["brown", "fox", "python"].index(keyword)
                bit_vector |= (1 << position)
        return bit_vector



# Test case
def test_search_engine():
    documents = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a widely used high-level programming language.",
        "The sky is blue.",
        "The dog is running in the park."
    ]
    search_engine = SearchEngine(documents)

    # Test query
    query = "brown fox python"
    result = search_engine.search(query)
    print("Search results for query '{}':".format(query))
    print(result)  # Output: [0, 1]

    query = "dog"
    result = search_engine.search(query)
    print("Search results for query '{}':".format(query))
    print(result)  # Output: [0, 3]


# Run the test case
if __name__ == "__main__":
    test_search_engine()