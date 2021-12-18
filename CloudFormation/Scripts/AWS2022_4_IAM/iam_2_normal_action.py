import boto3

iam = boto3.resource('iam')
iam_c = boto3.client('iam')


def attach_user_to_group(username, groupname):
    result = iam_c.add_user_to_group(UserName=username, GroupName=groupname)
    return result


def change_user_password(username, password, reset_required=False):
    try:
        iam_c.create_login_profile(
            Password=password,
            UserName=username,
            PasswordResetRequired=reset_required)
    except Exception as e:
        print(e)
        iam_c.update_login_profile(
            Password=password,
            UserName=username,
            PasswordResetRequired=reset_required)


def user_detail(username):
    result = iam_c.get_user(UserName=username).get('User')
    return {'username_e': username,
            'username_c': result.get('Tags')[0].get('Value') if result.get('Tags') else '',
            'user_id': result.get('UserId'),
            'arn': result.get('Arn'),
            'groups': get_user_group(username),
            }


def create_user(username, username_c, password, groupname, reset_required=False):
    iam.create_user(UserName=username,
                    Tags=[{'Key': 'Name', 'Value': username_c}])
    change_user_password(username, password, reset_required)
    attach_user_to_group(username, groupname)
    return user_detail(username)


def list_all_groups():
    group_dict = {}
    groups = iam_c.list_groups()
    for group in groups.get('Groups'):
        group_dict[group.get('GroupName')] = [group.get('GroupId'), group.get('Arn')]
    return group_dict


def get_group(group_name):
    group_detail = iam_c.get_group(GroupName=group_name)
    return {'group_name': group_name,
            'group_id': group_detail.get('Group').get('GroupId'),
            'arn': group_detail.get('Group').get('Arn'),
            'users': [x.get('UserName') for x in group_detail.get('Users')]}


def get_all_users():
    user_list = []
    for user in iam_c.list_users()['Users']:
        user_list.append(user.get('UserName'))
    return user_list


def get_user_group(username):
    group_list = []
    result = iam_c.list_groups_for_user(UserName=username)
    for group in result.get('Groups'):
        group_list.append(group.get('GroupName'))
    return group_list


def user_remove_out_group(username, groupname):
    iam_c.remove_user_from_group(
        GroupName=groupname,
        UserName=username
    )


def delete_user(username):
    for group in user_detail(username).get('groups'):
        user_remove_out_group(username, group)
    try:
        iam_c.delete_user(UserName=username)
    except Exception:
        iam_c.delete_login_profile(UserName=username)
        iam_c.delete_user(UserName=username)


if __name__ == '__main__':
    print(list_all_groups())
    # print(get_group('QytangIAMGroup'))
    # print(create_user('test1', '测试用户', 'Cisc0123', 'QytangIAMGroup'))
    # print(attach_user_to_group('test1', 'QytangIAMGroup'))
    # user_remove_out_group('test1', 'QytangIAMGroup')
    # change_user_password(username='test1', password='Cisc0123')  # 修改密码速度过快会出bug
    # print(get_all_users())
    # print(user_detail('test1'))
    # delete_user('test1')
    # print(get_user_group('test1'))  # 查询User的所属Group
    # for user in get_group('QytangIAMGroup').get('users'):  # 删除qytang_iam_group的所有用户
    #     delete_user(user)


