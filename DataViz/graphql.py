from enum import StrEnum


class Queries(StrEnum):
    BADGES = """
        query userBadges($username: String!) {
            matchedUser(username: $username) {
                badges {
                    id
                    name
                    shortName
                    displayName
                    icon
                    hoverText
                    medal {
                        slug
                        config {
                            iconGif
                            iconGifBackground
                        }
                    }
                    creationDate
                    category
                }
                upcomingBadges {
                    name
                    icon
                    progress
                }
            }
        }
    """
    PROBLEMS_SOLVED = """
        query userProblemsSolved($username: String!) {
            allQuestionsCount {
                difficulty
                count
            }
            matchedUser(username: $username) {
                problemsSolvedBeatsStats {
                    difficulty
                    percentage
                }
                submitStatsGlobal {
                    acSubmissionNum {
                        difficulty
                        count
                    }
                }
            }
        }
    """
    SKILL_STATS = """
        query skillStats($username: String!) {
            matchedUser(username: $username) {
                tagProblemCounts {
                    advanced {
                        tagName
                        tagSlug
                        problemsSolved
                    }
                    intermediate {
                        tagName
                        tagSlug
                        problemsSolved
                    }
                    fundamental {
                        tagName
                        tagSlug
                        problemsSolved
                    }
                }
            }
        }
    """
    LANGUAGE_STATS = """
        query languageStats($username: String!) {
            matchedUser(username: $username) {
                languageProblemCount {
                    languageName
                    problemsSolved
                }
            }
        }
    """
    RECENT_SUBMISSIONS = """
        query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            submitStats: submitStatsGlobal {
            acSubmissionNum {
                difficulty
                count
                submissions
            }
            }
        }
        recentSubmissionList(username: $username) {
            title
            titleSlug
            timestamp
            statusDisplay
            lang
            __typename
            }
        }
    """

class Variables(StrEnum):
    USERNAME = "chmod711"
