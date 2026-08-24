import requests
import xml.etree.ElementTree as ET

BASE_URL = "http://export.arxiv.org/api/query"

def search_arxiv(query: str, max_results: int = 5):
    params = {
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": max_results,
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()  # raise an error if the request failed

    root = ET.fromstring(response.text)

    for element in root.iter():
        element.tag = element.tag.split("}")[-1]

    papers = []
    for entry in root.findall("entry"):
        title = entry.find("title").text.strip()
        summary = entry.find("summary").text.strip()
        link = entry.find("id").text.strip()
        authors = [author.find("name").text for author in entry.findall("author")]
        papers.append({
            "title": title,
            "authors": authors,
            "summary": summary,
            "link": link,
        })
    return papers

if __name__ == "__main__":
    results = search_arxiv("large language models", max_results=3)
    for i, paper in enumerate(results, start=1):
        print(f"\n[{i}] {paper['title']}")
        print("Authors:", ", ".join(paper["authors"]))
        print("Link:", paper["link"])
        print("Summary:", paper["summary"][:200], "...")
