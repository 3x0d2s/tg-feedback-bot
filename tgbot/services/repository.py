import typing


class Repo:
    """Db abstraction layer"""

    def __init__(self, conn):
        self.conn = conn

    async def check_user_is_operator(self, user_tg_id) -> bool:
        """Проверяет является ли юзер оператором."""
        check = await self.conn.fetchval(
            "SELECT EXISTS(SELECT 1 FROM Operators WHERE tg_id=$1)",
            user_tg_id,
        )
        return check

    async def add_ticket(self, client_tg_id, ticket_text, datetime_msg) -> None:
        """Добавляет новый тикет."""
        await self.conn.execute(
            "INSERT INTO Tickets (client_tg_id, ticket_text, datetime_msg) VALUES ($1, $2, $3)",
            client_tg_id, ticket_text, datetime_msg
        )
        return

    async def list_tickets(self) -> typing.List[tuple]:
        """Возвращает список тикетов."""
        tickets = await self.conn.fetch(
            "SELECT * FROM Tickets ORDER BY datetime_msg"
        )
        return [{"id": ticket[0],
                 "client_tg_id": ticket[1],
                 "ticket_text": ticket[2],
                 "datetime_msg": ticket[3]} for ticket in tickets]

    async def close_ticket(self, client_tg_id) -> None:
        """Удаляет тикет, который создал определённый пользователь."""
        await self.conn.execute(
            "DELETE FROM Tickets WHERE client_tg_id=$1",
            client_tg_id
        )

    async def list_freedom_operators(self) -> typing.List[int]:
        """Возвращает список готовых взять тикет операторов."""
        operator_tg_ids = await self.conn.fetch(
            "SELECT tg_id FROM Operators WHERE is_ready=True"
        )
        return [operator_tg_id[0] for operator_tg_id in operator_tg_ids]

    async def add_dialog(self, operator_tg_id, client_tg_id) -> None:
        """Добавляет новый диалог."""
        await self.conn.execute(
            "INSERT INTO Dialogs (operator_tg_id, client_tg_id) VALUES ($1, $2)",
            operator_tg_id, client_tg_id
        )
        return

    async def check_user_in_dialog(self, user_tg_id) -> bool:
        """Проверяет состоит ли юзер в каком-либо диалоге."""
        check = await self.conn.fetchval(
            "SELECT EXISTS(SELECT 1 FROM Dialogs WHERE operator_tg_id=$1 OR client_tg_id=$1)",
            user_tg_id,
        )
        return check

    async def get_dialog_data(self, user_in_dialog_tg_id) -> typing.Tuple:
        """Возвращает информацию о диалоге."""
        dialog_data = await self.conn.fetchrow(
            "SELECT * FROM Dialogs WHERE operator_tg_id=$1 OR client_tg_id=$1",
            user_in_dialog_tg_id
        )
        return {
            "id": dialog_data[0],
            "operator_tg_id": dialog_data[1],
            "client_tg_id": dialog_data[2]
        }

    async def close_dialog(self, operator_tg_id) -> None:
        """Удаляет диалог, в котором находится указанный оператор."""
        await self.conn.execute(
            "DELETE FROM Dialogs WHERE operator_tg_id=$1",
            operator_tg_id
        )

    async def get_operator_data(self, operator_id=None, operator_tg_id=None) -> typing.Tuple:
        """Возвращает всю информацию об операторе."""
        if operator_id != None:
            operator_data = await self.conn.fetchrow(
                "SELECT * FROM Operators WHERE id=$1",
                operator_id
            )
        elif operator_tg_id != None:
            operator_data = await self.conn.fetchrow(
                "SELECT * FROM Operators WHERE tg_id=$1",
                operator_tg_id
            )
        return {
            "id": operator_data[0],
            "tg_id": operator_data[1],
            "name": operator_data[2],
            "is_ready": operator_data[3]
        }
