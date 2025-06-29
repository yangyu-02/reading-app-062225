# 📚 Reading App Implementation Roadmap

## 🏗️ Architecture Overview

**Backend:** Python + FastAPI + GraphQL (Strawberry) + SQLAlchemy Core + PostgreSQL + WorkOS Auth  
**Frontend:** React 19 + TypeScript + Apollo Client + shadcn/ui + Tailwind CSS  
**Deployment:** AWS Fargate + S3 + RDS PostgreSQL  
**Future:** iOS mobile app (React Native)

### Key Architectural Decisions

- **Backend:** Multi-app monolith structure (auth, documents, reading, chat apps)
- **Database:** SQLAlchemy Core (no ORM), Repository + Unit of Work patterns
- **Frontend:** Hybrid folder structure (features/ + shared/), GraphQL codegen
- **State:** React state + Apollo cache (no additional state management)
- **Testing:** Pytest (backend), Vitest + React Testing Library (frontend)
- **Auth:** Email/password initially, WorkOS integration later

### Backend Folder Structure (Implemented)

```
src/backend/
├── apps/
│   ├── auth/          # Authentication & user management
│   ├── documents/     # File upload & document processing
│   ├── reading/       # Reading progress & analytics
│   └── chat/          # AI chat functionality
├── shared/            # Cross-app utilities
├── core/              # App configuration & bootstrap
└── tests/             # Test organization mirrors apps/
```

Each app contains: `models.py`, `schemas.py`, `services.py`, `routes.py`

---

## 📋 Phase 1: Core MVP (Weeks 1-4)

### Backend Foundation

#### ✅ Project Setup & Dependencies

- [x] **Set up project structure**
  - [x] Create apps/ (auth, documents, reading, chat) folder structure
  - [x] Create shared/ utilities and core/ configuration folders
  - [ ] Set up bootstrap.py for dependency injection
  - [ ] Configure alembic for database migrations
- [x] **Install & configure core dependencies**
  - [x] FastAPI with CORS middleware for frontend
  - [x] Strawberry GraphQL with subscriptions support
  - [x] SQLAlchemy Core with asyncpg driver
  - [x] Redis for Dramatiq background jobs
  - [x] Email/password authentication (passlib + python-jose)
- [ ] **Development environment**
  - [ ] Docker compose for local PostgreSQL + Redis
  - [ ] Environment variable management with pydantic-settings
  - [ ] Ruff configuration for linting/formatting

#### ✅ Authentication & User Management

- [ ] **Email/Password Authentication**
  - [ ] User registration with email validation
  - [ ] Password hashing with bcrypt
  - [ ] JWT token generation and validation
  - [ ] Login/logout endpoints
- [ ] **WorkOS Integration (Future)**
  - [ ] Set up WorkOS organization and API keys
  - [ ] Create WorkOS authentication adapter
  - [ ] Migrate from email/password to WorkOS
- [ ] **User Domain Models**
  - [ ] User entity in domain layer (pure Python class)
  - [ ] User repository interface (abstract)
  - [ ] User repository implementation with SQLAlchemy Core
- [ ] **GraphQL Authentication**
  - [ ] Authentication directive for protected resolvers
  - [ ] User context injection in GraphQL
  - [ ] Login/logout mutations

#### ✅ Document Upload & Processing

- [ ] **File Storage Setup**
  - [ ] AWS S3 bucket configuration
  - [ ] S3 adapter for file operations (upload/download/delete)
  - [ ] File type validation (PDF, EPUB, DOCX, TXT)
  - [ ] File size limits and security checks
- [ ] **Document Processing**
  - [ ] AWS Textract integration for PDF parsing
  - [ ] Document content extraction to structured format
  - [ ] Chapter/section detection and storage
  - [ ] Background job for document processing using Dramatiq
- [ ] **Document Domain Models**
  - [ ] Document entity with metadata (title, author, page_count)
  - [ ] Chapter entity with content and word_count
  - [ ] Document repository with SQLAlchemy Core queries
- [ ] **GraphQL Document API**
  - [ ] File upload mutation with multipart support
  - [ ] Document queries (list, get by ID)
  - [ ] Document deletion with S3 cleanup

#### ✅ Reading Progress Tracking

- [ ] **Progress Domain Models**
  - [ ] ReadingProgress entity (user_id, document_id, current_page, last_read)
  - [ ] Page-level progress tracking
  - [ ] Reading session analytics
- [ ] **Progress Repository**
  - [ ] Upsert progress with conflict resolution
  - [ ] Query progress by user and document
  - [ ] Reading statistics aggregation
- [ ] **GraphQL Progress API**
  - [ ] Update progress mutation
  - [ ] Get progress query
  - [ ] Reading analytics query

#### ✅ AI Chat Integration

- [ ] **AI Service Setup**
  - [ ] OpenAI/Anthropic API integration
  - [ ] Chat context management with document content
  - [ ] Token usage tracking and limits
- [ ] **Chat Domain Models**
  - [ ] ChatSession entity (user_id, document_id)
  - [ ] ChatMessage entity (role, content, timestamp)
  - [ ] Chat repository for message storage
- [ ] **Real-time Chat**
  - [ ] GraphQL subscription for chat messages
  - [ ] WebSocket connection handling
  - [ ] Typing indicators and message status

### Frontend Foundation

#### ✅ Project Setup & Dependencies

- [ ] **Folder Structure Setup**
  - [ ] Create features/ (reading, chat, upload, auth)
  - [ ] Create shared/components/ and shared/hooks/
  - [ ] Set up GraphQL codegen configuration
- [ ] **Development Tools**
  - [ ] Vitest + React Testing Library setup
  - [ ] ESLint + Prettier configuration
  - [ ] TypeScript strict mode configuration

#### ✅ Authentication UI

- [ ] **Auth Components**
  - [ ] Login page with WorkOS integration
  - [ ] Protected route wrapper component
  - [ ] User profile component
  - [ ] Logout functionality
- [ ] **Auth Hooks**
  - [ ] useAuth hook for authentication state
  - [ ] useProtectedRoute hook
  - [ ] Token refresh handling

#### ✅ Document Upload Interface

- [ ] **Upload Components**
  - [ ] Drag & drop file upload component
  - [ ] File validation and preview
  - [ ] Upload progress indicator
  - [ ] File type icons and metadata display
- [ ] **Upload Hooks**
  - [ ] useDocumentUpload hook with Apollo mutation
  - [ ] useFileValidation hook
  - [ ] Upload error handling

#### ✅ Reading Interface

- [ ] **Reading Components**
  - [ ] Document viewer with pagination
  - [ ] Progress bar and page navigation
  - [ ] Table of contents/chapter navigation
  - [ ] Reading settings (font size, theme)
- [ ] **Reading Hooks**
  - [ ] useReadingProgress hook
  - [ ] useDocumentContent hook
  - [ ] Progress auto-save functionality

#### ✅ Chat Interface

- [ ] **Chat Components**
  - [ ] Chat message list with virtualization
  - [ ] Message input with send button
  - [ ] Typing indicators
  - [ ] Message status indicators
- [ ] **Chat Hooks**
  - [ ] useChatSubscription hook for real-time messages
  - [ ] useSendMessage hook
  - [ ] Chat history management

---

## ✨ Phase 2: Enhanced UX (Weeks 5-7)

### Backend Enhancements

#### ✅ Offline Support Infrastructure

- [ ] **API Design for Offline**
  - [ ] Conflict resolution strategies for progress sync
  - [ ] Batch operation endpoints
  - [ ] Data versioning for sync
- [ ] **Background Sync Jobs**
  - [ ] Queue offline actions for processing
  - [ ] Retry mechanisms for failed syncs
  - [ ] Conflict resolution algorithms

#### ✅ Performance Optimizations

- [ ] **Database Optimizations**
  - [ ] Query optimization and indexing
  - [ ] Connection pooling configuration
  - [ ] Read replica setup for analytics
- [ ] **Caching Strategy**
  - [ ] Redis caching for frequently accessed data
  - [ ] Document content caching
  - [ ] User session caching

### Frontend Enhancements

#### ✅ Offline Support

- [ ] **Apollo Client Configuration**
  - [ ] Cache persistence to localStorage
  - [ ] Offline mutation queuing
  - [ ] Network status detection
- [ ] **Offline UI States**
  - [ ] Offline indicator component
  - [ ] Sync status notifications
  - [ ] Conflict resolution UI

#### ✅ Loading States & Skeletons

- [ ] **Skeleton Components**
  - [ ] Document list skeleton
  - [ ] Reading interface skeleton
  - [ ] Chat message skeleton
  - [ ] Upload progress skeleton
- [ ] **Loading States**
  - [ ] Smart loading indicators
  - [ ] Error state components
  - [ ] Retry mechanisms

#### ✅ Progress Persistence

- [ ] **Local Storage Management**
  - [ ] Reading position backup
  - [ ] Settings persistence
  - [ ] Cache management
- [ ] **Sync Mechanisms**
  - [ ] Auto-sync on network reconnection
  - [ ] Manual sync triggers
  - [ ] Conflict resolution UI

#### ✅ Keyboard Shortcuts

- [ ] **Navigation Shortcuts**
  - [ ] Page forward/backward (arrow keys)
  - [ ] Chapter navigation (Ctrl+arrow)
  - [ ] Search (Ctrl+F)
  - [ ] Toggle chat (Ctrl+K)
- [ ] **Reading Shortcuts**
  - [ ] Font size adjustment
  - [ ] Theme toggle
  - [ ] Bookmark current page

#### ✅ Dark Mode

- [ ] **Theme Implementation**
  - [ ] Theme provider setup
  - [ ] System preference detection
  - [ ] Theme persistence
  - [ ] Smooth theme transitions
- [ ] **Component Theming**
  - [ ] Update all components for dark mode
  - [ ] Reading-friendly dark theme
  - [ ] High contrast options

#### ✅ Accessibility

- [ ] **Screen Reader Support**
  - [ ] ARIA labels and descriptions
  - [ ] Semantic HTML structure
  - [ ] Focus management
- [ ] **Keyboard Navigation**
  - [ ] Tab order optimization
  - [ ] Skip links
  - [ ] Keyboard shortcuts documentation
- [ ] **Visual Accessibility**
  - [ ] Color contrast compliance
  - [ ] Font size controls
  - [ ] Motion preference respect

---

## 📱 Phase 3: Mobile Preparation (Week 8)

### Backend Mobile Optimization

#### ✅ Push Notifications

- [ ] **Notification Infrastructure**
  - [ ] AWS SNS setup for push notifications
  - [ ] Device token management
  - [ ] Notification preferences
- [ ] **Notification Types**
  - [ ] Reading reminders
  - [ ] AI chat responses
  - [ ] Document processing completion

#### ✅ Mobile API Optimizations

- [ ] **Data Usage Optimization**
  - [ ] Paginated responses
  - [ ] Compressed document content
  - [ ] Minimal GraphQL responses
- [ ] **Background Processing**
  - [ ] Long-running operation status
  - [ ] Background sync endpoints
  - [ ] Offline-first API design

### Frontend Mobile Preparation

#### ✅ Cross-Platform Patterns

- [ ] **Business Logic Extraction**
  - [ ] Move logic from components to hooks
  - [ ] Platform-agnostic state management
  - [ ] Shared utility functions
- [ ] **Touch-First UI**
  - [ ] Touch-friendly button sizes
  - [ ] Swipe gestures for navigation
  - [ ] Mobile-optimized layouts

---

## 🧪 Testing Strategy

### Backend Testing

- [ ] **Unit Tests**
  - [ ] Domain model tests (pure functions)
  - [ ] Service layer tests with mocked repositories
  - [ ] Repository tests with test database
- [ ] **Integration Tests**
  - [ ] GraphQL resolver tests
  - [ ] Database integration tests
  - [ ] External service integration tests

### Frontend Testing

- [ ] **Component Tests**
  - [ ] UI component rendering tests
  - [ ] User interaction tests
  - [ ] Error state tests
- [ ] **Hook Tests**
  - [ ] Custom hook behavior tests
  - [ ] GraphQL operation tests
  - [ ] State management tests

---

## 🚀 Deployment & DevOps

### AWS Infrastructure

- [ ] **ECS Fargate Setup**
  - [ ] Container configuration
  - [ ] Load balancer setup
  - [ ] Auto-scaling configuration
- [ ] **Database & Storage**
  - [ ] RDS PostgreSQL setup
  - [ ] S3 bucket configuration
  - [ ] Redis ElastiCache setup
- [ ] **CI/CD Pipeline**
  - [ ] GitHub Actions workflow
  - [ ] Automated testing
  - [ ] Blue-green deployment

---

## 📊 Success Metrics

### Technical Metrics

- [ ] API response times < 200ms
- [ ] Frontend loading time < 2s
- [ ] 99.9% uptime
- [ ] Zero data loss

### User Experience Metrics

- [ ] Document upload success rate > 95%
- [ ] Reading progress sync accuracy > 99%
- [ ] Chat response time < 3s
- [ ] Mobile performance parity

---

## 🔧 Development Guidelines

- **Follow cursor rules** in `.cursorrules` files for both backend and frontend
- **Ask clarifying questions** before implementing features
- **Test early and often** with both unit and integration tests
- **Mobile-first considerations** for all decisions
- **Security-first approach** especially around file uploads and authentication
- **Performance monitoring** from day one

---

## 📝 Notes & Decisions Log

### Key Decisions Made

1. **No ORM** - Using SQLAlchemy Core for better control and performance
2. **No additional state management** - React + Apollo cache sufficient for this app
3. **GraphQL codegen** - Type safety and better developer experience
4. **Hybrid folder structure** - Balance between feature organization and reusability
5. **AWS Fargate** - Simplicity and cost-effectiveness for MVP

### Future Considerations

- **Mobile app development** - React Native with shared business logic
- **Advanced analytics** - Reading patterns and user insights
- **Social features** - Book sharing and community features
- **Enterprise features** - Team accounts and admin dashboards
