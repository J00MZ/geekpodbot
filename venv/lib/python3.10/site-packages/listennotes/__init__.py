import re
import logging
from requests_cache import CachedSession
from datetime import timedelta

LOG = logging.getLogger("PodcastsAPI")


class ListenNotes:
    _genres = []
    _langs = []
    base_url = "http://listen-api.listennotes.com/"
    session = CachedSession(backend='memory', expire_after=timedelta(hours=3))

    def __init__(self, key):
        self.key = key

    def get_langs(self):
        try:
            return self.session.get(self.base_url + "v2/languages",
                                    headers= self._headers).json()["languages"]
        except:
            return ['Any language',
                    'Afar',
                    'Abkhazian',
                    'Afrikaans',
                    'Akan',
                    'Albanian',
                    'Arabic',
                    'Azerbaijani',
                    'Bambara',
                    'Bashkir',
                    'Basque',
                    'Belarusian',
                    'Bulgarian',
                    'Catalan',
                    'Chamorro',
                    'Chinese',
                    'Croatian',
                    'Czech',
                    'Danish',
                    'Dutch',
                    'English',
                    'Estonian',
                    'Faeroese',
                    'Finnish',
                    'French',
                    'Gaelic',
                    'Galician',
                    'German',
                    'Greek',
                    'Hebrew',
                    'Hindi',
                    'Hungarian',
                    'Icelandic',
                    'Indonesian',
                    'Irish',
                    'Italian',
                    'Japanese',
                    'Khmer',
                    'Kirghiz',
                    'Korean',
                    'Latvian',
                    'Lithuanian',
                    'Macedonian',
                    'Malay',
                    'Nepali',
                    'Northern Sami',
                    'Norwegian',
                    'Polish',
                    'Portuguese',
                    'Romanian',
                    'Russian',
                    'Serbian',
                    'Singhalese',
                    'Slovak',
                    'Slovenian',
                    'Spanish',
                    'Swahili',
                    'Swedish',
                    'Thai',
                    'Turkish',
                    'Twi',
                    'Ukranian',
                    'Urdu',
                    'Vietnamese']

    def get_genres(self):
        try:
            headers = self._headers
            return self.session.get(self.base_url + "api/v2/genres",
                                headers=headers).json()["genres"]
        except:
            return [{'id': 139, 'name': 'VR & AR', 'parent_id': 127},
                    {'id': 140, 'name': 'Web Design', 'parent_id': 127},
                    {'id': 141, 'name': 'Golf', 'parent_id': 77},
                    {'id': 142, 'name': 'English Learning', 'parent_id': 116},
                    {'id': 143, 'name': 'Programming', 'parent_id': 127},
                    {'id': 144, 'name': 'Personal Finance', 'parent_id': 67},
                    {'id': 145, 'name': 'Parenting', 'parent_id': 132},
                    {'id': 146, 'name': 'LGBTQ', 'parent_id': 122},
                    {'id': 147, 'name': 'SEO', 'parent_id': 97},
                    {'id': 148, 'name': 'American History', 'parent_id': 125},
                    {'id': 149, 'name': 'Venture Capital', 'parent_id': 93},
                    {'id': 138, 'name': 'Movie', 'parent_id': 68},
                    {'id': 150, 'name': 'Chinese History', 'parent_id': 125},
                    {'id': 151, 'name': 'Locally Focused', 'parent_id': 67},
                    {'id': 154, 'name': 'San Francisco Bay Area',
                     'parent_id': 152},
                    {'id': 155, 'name': 'Denver', 'parent_id': 152},
                    {'id': 157, 'name': 'Startup', 'parent_id': 93},
                    {'id': 158, 'name': 'NFL', 'parent_id': 78},
                    {'id': 159, 'name': 'Harry Potter', 'parent_id': 68},
                    {'id': 162, 'name': 'Game of Thrones', 'parent_id': 68},
                    {'id': 165, 'name': 'Storytelling', 'parent_id': 122},
                    {'id': 166, 'name': 'YouTube', 'parent_id': 68},
                    {'id': 83, 'name': 'Other Games', 'parent_id': 82},
                    {'id': 84, 'name': 'Automotive', 'parent_id': 82},
                    {'id': 85, 'name': 'Video Games', 'parent_id': 82},
                    {'id': 86, 'name': 'Hobbies', 'parent_id': 82},
                    {'id': 87, 'name': 'Aviation', 'parent_id': 82},
                    {'id': 152, 'name': 'United States', 'parent_id': 151},
                    {'id': 156, 'name': 'China', 'parent_id': 151},
                    {'id': 160, 'name': 'Star Wars', 'parent_id': 68},
                    {'id': 163, 'name': 'AI & Data Science', 'parent_id': 127},
                    {'id': 67, 'name': 'Podcasts', 'parent_id': None},
                    {'id': 68, 'name': 'TV & Film', 'parent_id': 67},
                    {'id': 69, 'name': 'Religion & Spirituality',
                     'parent_id': 67},
                    {'id': 70, 'name': 'Spirituality', 'parent_id': 69},
                    {'id': 71, 'name': 'Islam', 'parent_id': 69},
                    {'id': 72, 'name': 'Buddhism', 'parent_id': 69},
                    {'id': 73, 'name': 'Judaism', 'parent_id': 69},
                    {'id': 74, 'name': 'Other', 'parent_id': 69},
                    {'id': 75, 'name': 'Christianity', 'parent_id': 69},
                    {'id': 76, 'name': 'Hinduism', 'parent_id': 69},
                    {'id': 77, 'name': 'Sports & Recreation', 'parent_id': 67},
                    {'id': 78, 'name': 'Professional', 'parent_id': 77},
                    {'id': 79, 'name': 'Outdoor', 'parent_id': 77},
                    {'id': 80, 'name': 'College & High School',
                     'parent_id': 77},
                    {'id': 81, 'name': 'Amateur', 'parent_id': 77},
                    {'id': 82, 'name': 'Games & Hobbies', 'parent_id': 67},
                    {'id': 88, 'name': 'Health', 'parent_id': 67},
                    {'id': 89, 'name': 'Fitness & Nutrition', 'parent_id': 88},
                    {'id': 90, 'name': 'Self-Help', 'parent_id': 88},
                    {'id': 91, 'name': 'Alternative Health', 'parent_id': 88},
                    {'id': 92, 'name': 'Sexuality', 'parent_id': 88},
                    {'id': 93, 'name': 'Business', 'parent_id': 67},
                    {'id': 94, 'name': 'Careers', 'parent_id': 93},
                    {'id': 95, 'name': 'Business News', 'parent_id': 93},
                    {'id': 96, 'name': 'Shopping', 'parent_id': 93},
                    {'id': 97, 'name': 'Management & Marketing',
                     'parent_id': 93},
                    {'id': 98, 'name': 'Investing', 'parent_id': 93},
                    {'id': 99, 'name': 'News & Politics', 'parent_id': 67},
                    {'id': 100, 'name': 'Arts', 'parent_id': 67},
                    {'id': 101, 'name': 'Performing Arts', 'parent_id': 100},
                    {'id': 102, 'name': 'Food', 'parent_id': 100},
                    {'id': 103, 'name': 'Visual Arts', 'parent_id': 100},
                    {'id': 104, 'name': 'Literature', 'parent_id': 100},
                    {'id': 105, 'name': 'Design', 'parent_id': 100},
                    {'id': 106, 'name': 'Fashion & Beauty', 'parent_id': 100},
                    {'id': 107, 'name': 'Science & Medicine', 'parent_id': 67},
                    {'id': 108, 'name': 'Social Sciences', 'parent_id': 107},
                    {'id': 109, 'name': 'Medicine', 'parent_id': 107},
                    {'id': 110, 'name': 'Natural Sciences', 'parent_id': 107},
                    {'id': 111, 'name': 'Education', 'parent_id': 67},
                    {'id': 112, 'name': 'Educational Technology',
                     'parent_id': 111},
                    {'id': 113, 'name': 'Higher Education', 'parent_id': 111},
                    {'id': 114, 'name': 'K-12', 'parent_id': 111},
                    {'id': 115, 'name': 'Training', 'parent_id': 111},
                    {'id': 116, 'name': 'Language Courses', 'parent_id': 111},
                    {'id': 117, 'name': 'Government & Organizations',
                     'parent_id': 67},
                    {'id': 118, 'name': 'Local', 'parent_id': 117},
                    {'id': 136, 'name': 'Crypto & Blockchain',
                     'parent_id': 127},
                    {'id': 135, 'name': 'True Crime', 'parent_id': 122},
                    {'id': 119, 'name': 'Non-Profit', 'parent_id': 117},
                    {'id': 120, 'name': 'Regional', 'parent_id': 117},
                    {'id': 121, 'name': 'National', 'parent_id': 117},
                    {'id': 122, 'name': 'Society & Culture', 'parent_id': 67},
                    {'id': 123, 'name': 'Places & Travel', 'parent_id': 122},
                    {'id': 124, 'name': 'Personal Journals', 'parent_id': 122},
                    {'id': 126, 'name': 'Philosophy', 'parent_id': 122},
                    {'id': 128, 'name': 'Software How-To', 'parent_id': 127},
                    {'id': 129, 'name': 'Podcasting', 'parent_id': 127},
                    {'id': 130, 'name': 'Gadgets', 'parent_id': 127},
                    {'id': 131, 'name': 'Tech News', 'parent_id': 127},
                    {'id': 132, 'name': 'Kids & Family', 'parent_id': 67},
                    {'id': 133, 'name': 'Comedy', 'parent_id': 67},
                    {'id': 134, 'name': 'Music', 'parent_id': 67},
                    {'id': 153, 'name': 'New York', 'parent_id': 152},
                    {'id': 161, 'name': 'Star Trek', 'parent_id': 68},
                    {'id': 164, 'name': 'Apple', 'parent_id': 127},
                    {'id': 125, 'name': 'History', 'parent_id': 122},
                    {'id': 137, 'name': 'NBA', 'parent_id': 78},
                    {'id': 127, 'name': 'Technology', 'parent_id': 67},
                    {'id': 167, 'name': 'Audio Drama', 'parent_id': 122},
                    {'id': 168, 'name': 'Fiction', 'parent_id': 122},
                    {'id': 169, 'name': 'Sales', 'parent_id': 93}]

    @property
    def _headers(self):
        return {
            "X-ListenAPI-Key": self.key,
            "Accept": "application/json"
        }

    @property
    def genre_names(self):
        return [g["name"] for g in self.genres]

    @property
    def genres(self):
        if not self._genres:
            self._genres = self.get_genres()
        return self._genres

    @property
    def langs(self):
        if not self._langs:
            self._langs = self.get_langs()
        return self._langs

    def genre_to_id(self, name):
        for genre in self.genres:
            if genre["name"] == name:
                return genre["id"]
        return None

    def id_to_genre(self, genre_id):
        for genre in self.genres:
            if int(genre["id"]) == int(genre_id):
                return genre["name"]
        return None

    def search(self, query, published_before="", published_after="",
               genres=None, safe_mode=1, max_len=90, min_len=0, offset=0,
               lang="en-us", sort_by_relevance=True, search_type="podcast",
               only_in=""):
        base_url = self.base_url + "api/v2/search"

        if lang not in self.langs:
            if lang.startswith("en"):
                lang = "English"
            else:
                # TODO lang support
                lang = "Any Language"

        genres = genres or []

        params = {"sort_by_date": int(not sort_by_relevance),
                  "safe_mode": safe_mode,
                  "q": query,
                  "language": lang,
                  "type": search_type,
                  "offset": offset}
        if only_in:
            params["only_in"] = only_in

        if genres:
            for idx, genre in enumerate(genres):
                if isinstance(genre, dict):
                    genres[idx] = int(genre.get("id"))
                elif isinstance(genre, str):
                    if not genre.isdigit():
                        genres[idx] = self.genre_to_id(genre)
                    else:
                        genres[idx] = int(genre)

            params["genre_ids"] = genres

        response = self.session.get(base_url, params=params,
                                    headers=self._headers)

        return self._pretty_search_result(response.json())

    def search_episode(self, query, published_before="", published_after="",
                       genres=None, safe_mode=1, max_len=90, min_len=0,
                       offset=0,
                       lang="en-us", sort_by_relevance=False):
        return self.search(query, published_before, published_after, genres,
                           safe_mode, max_len, min_len, offset, lang,
                           sort_by_relevance, search_type="episode")

    def search_podcast(self, query, published_before="", published_after="",
                       genres=None, safe_mode=1, max_len=90, min_len=0,
                       offset=0,
                       lang="en-us", sort_by_relevance=True):
        return self.search(query, published_before, published_after, genres,
                           safe_mode, max_len, min_len, offset, lang,
                           sort_by_relevance, search_type="podcast")

    def search_by_genre(self, query, genres, published_before="",
                        published_after="", safe_mode=1, max_len=90,
                        min_len=0, offset=0, lang="en-us",
                        sort_by_relevance=True):
        if isinstance(genres, str) or isinstance(genres, int):
            genres = [genres]
        for g in genres:
            try:
                g_id = int(g)
                if not g_id:
                    LOG.warning("unknown genre id: " + g_id)
                else:
                    LOG.info("podcast genre:" + self.id_to_genre(g_id))
            except:
                g_id = self.genre_to_id(g)
                if not g_id:
                    LOG.warning("unknown genre: " + g)
                else:
                    LOG.info("podcast genre:" + self.id_to_genre(g))
        return self.search(query, published_before, published_after, genres,
                           safe_mode, max_len, min_len, offset, lang,
                           sort_by_relevance, search_type="podcast")

    def search_episode_in_title(self, query, published_before="",
                                published_after="",
                                genres=None, safe_mode=1, max_len=90,
                                min_len=0, offset=0,
                                lang="en-us", sort_by_relevance=True):
        return self.search(query, published_before, published_after, genres,
                           safe_mode, max_len, min_len, offset, lang,
                           sort_by_relevance, only_in="title",
                           search_type="episode")

    def search_podcast_in_title(self, query, published_before="",
                                published_after="",
                                genres=None, safe_mode=1, max_len=90,
                                min_len=0, offset=0,
                                lang="en-us", sort_by_relevance=True):
        return self.search(query, published_before, published_after, genres,
                           safe_mode, max_len, min_len, offset, lang,
                           sort_by_relevance,
                           only_in="title", search_type="podcast")

    def search_episode_in_author(self, query, published_before="",
                                 published_after="",
                                 genres=None, safe_mode=1, max_len=90,
                                 min_len=0, offset=0,
                                 lang="en-us", sort_by_relevance=True):
        return self.search(query, published_before, published_after, genres,
                           safe_mode, max_len, min_len, offset, lang,
                           sort_by_relevance,
                           only_in="author",
                           search_type="episode")

    def search_podcast_in_author(self, query, published_before="",
                                 published_after="",
                                 genres=None, safe_mode=1, max_len=90,
                                 min_len=0, offset=0,
                                 lang="en-us", sort_by_relevance=True):
        return self.search(query, published_before, published_after, genres,
                           safe_mode, max_len, min_len, offset, lang,
                           sort_by_relevance,
                           only_in="author", search_type="podcast")

    def search_episode_in_description(self, query, published_before="",
                                      published_after="",
                                      genres=None, safe_mode=1, max_len=90,
                                      min_len=0, offset=0,
                                      lang="en-us", sort_by_relevance=True):
        return self.search(query, published_before, published_after, genres,
                           safe_mode, max_len, min_len, offset, lang,
                           sort_by_relevance,
                           only_in="description", search_type="episode")

    def search_podcast_in_description(self, query, published_before="",
                                      published_after="",
                                      genres=None, safe_mode=1, max_len=90,
                                      min_len=0, offset=0,
                                      lang="en-us", sort_by_relevance=True):
        return self.search(query, published_before, published_after, genres,
                           safe_mode, max_len, min_len, offset, lang,
                           sort_by_relevance,
                           only_in="description", search_type="podcast")

    def get_episodes(self, podcast_id):
        if isinstance(podcast_id, list):
            podcast_id = podcast_id[0]
        if isinstance(podcast_id, dict):
            podcast_id = podcast_id["id"]

        data = self.session.get(
            self.base_url + "api/v2/podcasts/" + str(podcast_id),
            headers=self._headers).json()
        if not data:
            podcast_id = self.search_podcast(podcast_id)[0]["id"]
            data = self.session.get(
                self.base_url + "api/v2/podcasts/" + str(podcast_id),
                headers=self._headers).json()
        return self._pretty_episode_result(data)

    def _pretty_search_result(self, data):
        if "results" in data:
            data = data["results"]
        if not isinstance(data, list):
            data = [data]
        bucket = []
        for res in data:

            bucket.append({
                "description": self.remove_html(res["description_original"]),
                "explicit_content": res["explicit_content"],
                'genres': res['genre_ids'],
                "publisher": res["publisher_original"],
               # "rss": res["rss"],
                "id": res["id"],
                "episodes": self.get_episodes(res["id"]),
                "title": res["title_original"]})
            if "audio" in res:
                bucket[-1]["stream"] = res["audio"]
                bucket[-1]["audio_length"] = res["audio_length_sec"]
            elif "total_episodes" in res:
                bucket[-1]["total_episodes"] = res["total_episodes"]

        return bucket

    def _pretty_episode_result(self, data):
        if "episodes" in data:
            data = data["episodes"]
        if not isinstance(data, list):
            data = [data]
        bucket = []
        for res in data:

            bucket.append({
                "description": self.remove_html(res["description"]),
                "explicit_content": res["explicit_content"],
                "id": res["id"],
                "title": res["title"]})
            if "audio" in res:
                bucket[-1]["stream"] = res["audio"]
                bucket[-1]["audio_length"] = res["audio_length_sec"]
        return bucket

    def _pretty_popular_result(self, data):
        if "podcasts" in data:
            data = data["podcasts"]
        elif "channels" in data:
            data = data["channels"]
        if not isinstance(data, list):
            data = [data]
        bucket = []
        for res in data:
            bucket.append({
                "country": res["country"],
                "description": self.remove_html(res["description"]),
                "explicit_content": res["explicit_content"],
                "id": res["id"],
                "publisher": res["publisher"],
                "title": res["title"]})
        return bucket

    def _pretty_random_result(self, res):
        bucket = {"description": self.remove_html(res["description"]),
                  "explicit_content": res["explicit_content"],
                  "id": res["id"],
                  'podcast_title': res['podcast_title'],
                  "title": res["title"],
                  "stream": res["audio"],
                  "audio_length": res["audio_length_sec"]}
        return bucket

    @staticmethod
    def remove_html(text):
        return re.sub('<[^>]*>', '', text).replace('  ', ' ')

    def get_popular(self):
        return self._pretty_popular_result(self.session.get(
            self.base_url + "api/v2/best_podcasts/",
            headers=self._headers).json())

    def random_podcast(self):
        return self._pretty_random_result(self.session.get(
            self.base_url + "api/v2/just_listen/",
            headers=self._headers).json())

