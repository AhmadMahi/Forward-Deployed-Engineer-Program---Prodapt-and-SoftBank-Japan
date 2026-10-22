# SmartDesk dashboard: build with Node, serve static files with an unprivileged nginx image.
FROM node:22-alpine AS build
WORKDIR /web
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginxinc/nginx-unprivileged:1.27-alpine
COPY --from=build /web/dist /usr/share/nginx/html
EXPOSE 8080
