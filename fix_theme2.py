import os
import re

directories = [
    'frontend/src/app/dashboard/page.tsx',
    'frontend/src/app/dashboard/memory/page.tsx',
    'frontend/src/app/dashboard/opportunities/page.tsx',
    'frontend/src/app/dashboard/opportunities/[id]/page.tsx'
]

def apply_fixes(content):
    # Fix the double dark classes introduced by the previous script
    content = content.replace('dark:text-zinc-400 dark:text-zinc-400', 'dark:text-zinc-400')
    
    # Fix the stray text-white on the search inputs
    content = content.replace('text-sm text-white focus:outline-none', 'text-sm text-zinc-900 dark:text-white focus:outline-none')
    
    # Ensure any remaining text-white outside of specific contexts gets dark mode handling
    # (Leaving it alone if it's already got dark: preceding it)
    return content

for file_path in directories:
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
            new_content = apply_fixes(content)
        with open(file_path, 'w') as f:
            f.write(new_content)
        print(f"Fixed {file_path}")
