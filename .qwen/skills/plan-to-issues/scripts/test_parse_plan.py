import unittest
from parse_plan import extract_tasks, detect_labels

class TestExtractTasks(unittest.TestCase):
    def test_extract_single_task(self):
        plan = """# Test Plan
---
### Task 1: Add API endpoint

**Files:**
- Create: `src/api/users.py`

**Step 1: Write test**
```python
def test_users_endpoint():
    pass
```

**Step 2: Run test**
Run: pytest tests/test_users.py
"""
        tasks = extract_tasks(plan)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['number'], 1)
        self.assertEqual(tasks[0]['title'], 'Add API endpoint')
        self.assertIn('Create: `src/api/users.py`', tasks[0]['files'])
        self.assertEqual(len(tasks[0]['steps']), 2)

    def test_extract_multiple_tasks(self):
        plan = """# Test Plan
---
### Task 1: Add user model

**Files:**
- Create: `src/models/user.py`

**Step 1: Write test**
test

**Step 2: Implement**
code

### Task 2: Add user tests

**Files:**
- Create: `tests/test_user.py`

**Step 1: Write test**
test code
"""
        tasks = extract_tasks(plan)
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]['title'], 'Add user model')
        self.assertEqual(tasks[1]['title'], 'Add user tests')

    def test_no_tasks(self):
        plan = "# Just a heading\n---\nNo tasks here."
        tasks = extract_tasks(plan)
        self.assertEqual(tasks, [])

if __name__ == '__main__':
    unittest.main()


class TestDetectLabels(unittest.TestCase):
    def test_single_label_match(self):
        task = {
            'title': 'Write tests for users',
            'files': '',
            'steps': [{'title': 'pytest', 'content': 'test code'}],
        }
        labels = detect_labels(task)
        self.assertIn('testing', labels)

    def test_multi_label_match(self):
        task = {
            'title': 'Add API endpoint',
            'files': '- Create: `src/api/users.py`',
            'steps': [{'title': 'Write test', 'content': 'test endpoint'}],
        }
        labels = detect_labels(task)
        self.assertIn('api', labels)
        self.assertIn('testing', labels)
        self.assertIn('enhancement', labels)

    def test_no_match_fallback(self):
        task = {
            'title': 'Do something xyz',
            'files': '',
            'steps': [{'title': 'Step', 'content': 'stuff'}],
        }
        labels = detect_labels(task)
        self.assertEqual(labels, ['task'])

    def test_database_label_detection(self):
        task = {
            'title': 'Create user model',
            'files': '- Create: `src/models/user.py`',
            'steps': [{'title': 'Write test', 'content': 'test model'}],
        }
        labels = detect_labels(task)
        self.assertIn('database', labels)

    def test_security_label_detection(self):
        task = {
            'title': 'Add auth middleware',
            'files': '- Create: `src/middleware/auth.py`',
            'steps': [{'title': 'Test validation', 'content': 'verify token'}],
        }
        labels = detect_labels(task)
        self.assertIn('security', labels)
