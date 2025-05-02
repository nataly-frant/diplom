# Этап 1: Билдим фронтенд
FROM node:18-slim AS build

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и package-lock.json
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем весь проект
COPY . .

# Билдим проект
RUN npm run build

# Этап 2: Минимальный образ с Nginx
FROM nginx:stable-alpine

# Копируем билд в папку Nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Копируем свой nginx.conf, если хочешь настроить роутинг для SPA
# (например, чтобы пути работали без 404)
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Открываем порт
EXPOSE 80

# Стартуем Nginx
CMD ["nginx", "-g", "daemon off;"]
