import json
import requests
from .graphql import Queries, Variables


BASE_URL = "https://leetcode.com/graphql/"

class Response:
    def __init__(self, query, url=BASE_URL):
        self.query_name = query.name
        self.content = requests.post(
            url
            , json={
                "query": query,
                "variables": json.dumps({
                    var.name.lower() : var.value
                    for var in Variables
                })
            }
        )
        self.content = json.loads(self.content.text)
        self.data = self.content["data"]

    def _get_data_by_field(self, field):
        if not field in self.data:
            raise KeyError(f"{field} is not a field in response from query {self.query_name}")
        return self.data[field]

    @property
    def allQuestionsCount(self):
        return self._get_data_by_field("allQuestionsCount")

    @property
    def matchedUser(self):
        return self._get_data_by_field("matchedUser")

    @property
    def recentSubmissionList(self):
        return self._get_data_by_field("recentSubmissionList")

if __name__ == "__main__":
    response = Response(
        query=Queries.PROBLEMS_SOLVED
    )

    print(response.allQuestionsCount)
    print(response.matchedUser)
