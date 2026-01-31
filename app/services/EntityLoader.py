from app.services.exceptions import *


class EntityLoader:
    def __init__(self, user_repo, task_repo, board_repo, notification_repo, report_repo, tag_repo):
        self.user_repo = user_repo
        self.task_repo = task_repo
        self.board_repo = board_repo
        self.notification_repo = notification_repo
        self.report_repo = report_repo
        self.tag_repo = tag_repo

    def get_user(self, user_id):
        user = self.user_repo.get_by_id(user_id)
        if user is None:
            raise UserIdNotFound(user_id)
        return user

    def get_task(self, task_id):
        task = self.task_repo.get_by_id(task_id)
        if task is None:
            raise TaskIdNotFound(task_id)
        return task

    def get_board(self, board_id):
        board = self.board_repo.get_by_id(board_id)
        if board is None:
            raise BoardIdNotFound(board_id)
        return board

    def get_notification(self, notification_id):
        notification = self.notification_repo.get_by_id(notification_id)
        if notification is None:
            raise NotificationIdNotFound(notification_id)
        return notification

    def get_tag(self, tag_name):
        tag = self.tag_repo.get_by_name(tag_name)
        if tag is None:
            raise TagNameNotFound(tag_name)
        return tag

    def get_report(self, report_id):
        report = self.report_repo.get_by_id(report_id)
        if report is None:
            raise ReportIdNotFound(report_id)
        return report