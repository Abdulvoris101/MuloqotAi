from datetime import datetime, date

from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request, Query, Depends
from fastapi.responses import HTMLResponse
from apps.core.models import Message, Chat, ChatActivity
from apps.core.managers import ChatManager, MessageManager, ChatActivityManager
from db.setup import session
from sqlalchemy import desc, Date, cast, func

templates = Jinja2Templates(directory="layout/templates")

router = APIRouter()


@router.get("/chats", response_class=HTMLResponse)
async def admin(request: Request, page: int = Query(1, gt=0)):
    rowsPerPage = 15
    offset = (page - 1) * rowsPerPage
    totalItems = ChatManager.usersCount()
    totalPages = (totalItems // rowsPerPage) + (1 if totalItems % rowsPerPage > 0 else 0)
    query = session.query(Chat).order_by(desc(Chat.id)).limit(rowsPerPage).offset(offset)

    return templates.TemplateResponse("index.html", {
        "chats": query.all(),
        "groups": ChatManager.groupsCount(),
        "messages": Message.count(),
        "activeUsers": ChatActivityManager.getCurrentMonthUsers(),
        "countOfAllInputTokens": ChatActivityManager.countTokens(columnName='inputTokens', today=False),
        "countOfAllOutputTokens": ChatActivityManager.countTokens(columnName='outputTokens', today=False),
        "request": request,
        "users": ChatManager.usersCount(),
        "all_chats": ChatManager.all(),
        "total_pages": totalPages,
        "current_page": page
    })


@router.get("/active_chats", response_class=HTMLResponse)
async def admin(request: Request, page: int = Query(1, gt=0)):
    rowsPerPage = 15
    offset = (page - 1) * rowsPerPage
    totalItems = ChatManager.usersCount()
    totalPages = (totalItems // rowsPerPage) + (1 if totalItems % rowsPerPage > 0 else 0)
    query = session.query(Chat).\
        join(Chat.chatActivity).\
        filter(ChatActivity.todaysMessages >= 1).\
        order_by(desc(Chat.id)).\
        limit(rowsPerPage).\
        offset(offset)

    return templates.TemplateResponse("active.html", {
        "chats": query.all(),
        "groups": ChatManager.groupsCount(),
        "messages": MessageManager.getTodayMessagesCount(),
        "activeUsers": ChatActivityManager.getCurrentMonthUsers(),
        "countOfAllInputTokens": ChatActivityManager.countTokens(columnName='inputTokens', today=True),
        "countOfAllOutputTokens": ChatActivityManager.countTokens(columnName='outputTokens', today=True),
        "request": request,
        "users": query.count(),
        "all_chats": ChatManager.all(),
        "total_pages": totalPages,
        "current_page": page
    })


@router.get("/systemMessages", response_class=HTMLResponse)
async def systemMessages(request: Request):
    return templates.TemplateResponse("system_messages.html", {
        "groups": ChatManager.groupsCount(),
        "messages": Message.count(),
        "countOfAllInputTokens": ChatActivityManager.countOfAllInputTokens(),
        "countOfAllOutputTokens": ChatActivityManager.countOfAllOutputTokens(),
        "activeUsers": ChatActivityManager.getCurrentMonthUsers(),
        "request": request,
        "users": ChatManager.usersCount(),
        "all_systemMessages": MessageManager.getSystemMessages()
    })

