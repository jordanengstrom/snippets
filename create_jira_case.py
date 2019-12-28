from jira import JIRA


def create_jira_ticket():
    options = {
        'server': 'https://jira.your-server-here.com'
    }

    jira = JIRA(options, basic_auth=('username', 'password'))

    issue_dict = {
        'project': 'URPRJT',
        'issuetype': {'name': 'issue-name-here'},
        'other_req_keys': 'other_req_vals'
    }

    new_issue = jira.create_issue(**issue_dict)
    print(new_issue)
    return new_issue.key


def main():
    pass


if __name__ == '__main__':
    main()
