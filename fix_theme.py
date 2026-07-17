import os
import re

directories = [
    'frontend/src/app/dashboard/page.tsx',
    'frontend/src/app/dashboard/memory/page.tsx',
    'frontend/src/app/dashboard/opportunities/page.tsx',
    'frontend/src/app/dashboard/opportunities/[id]/page.tsx'
]

replacements = [
    (r'bg-\[\#050505\] text-white', r'bg-zinc-50 dark:bg-[#050505] text-zinc-900 dark:text-white'),
    (r'bg-\[\#0a0a0a\]', r'bg-white dark:bg-[#0a0a0a]'),
    (r'border-white/10', r'border-zinc-200 dark:border-white/10'),
    (r'border-white/5', r'border-zinc-200 dark:border-white/5'),
    (r'bg-white/5', r'bg-zinc-100 dark:bg-white/5'),
    (r'text-zinc-400', r'text-zinc-600 dark:text-zinc-400'),
    (r'hover:bg-white/5', r'hover:bg-zinc-100 dark:hover:bg-white/5'),
    (r'hover:text-white', r'hover:text-zinc-900 dark:hover:text-white'),
    (r'bg-zinc-900/50', r'bg-white dark:bg-zinc-900/50'),
    (r'bg-zinc-900/30', r'bg-zinc-100 dark:bg-zinc-900/30'),
    (r'bg-zinc-900', r'bg-white dark:bg-zinc-900'),
    (r'hover:bg-zinc-800', r'hover:bg-zinc-100 dark:hover:bg-zinc-800'),
    (r'bg-zinc-800/50', r'bg-zinc-200 dark:bg-zinc-800/50'),
    (r'text-zinc-700', r'text-zinc-400 dark:text-zinc-700'),
    (r'text-zinc-500', r'text-zinc-500 dark:text-zinc-400'),
    (r'text-zinc-600', r'text-zinc-500 dark:text-zinc-600'),
    (r'text-white', r'text-zinc-900 dark:text-white'),  # This might be tricky, will do it carefully
]

def apply_replacements(content):
    # First, handle text-white carefully so we don't mess up existing dark:text-white
    content = content.replace('bg-[#050505] text-white', 'bg-zinc-50 dark:bg-[#050505] text-zinc-900 dark:text-white')
    content = content.replace('bg-[#0a0a0a]', 'bg-white dark:bg-[#0a0a0a]')
    content = content.replace('border-white/10', 'border-zinc-200 dark:border-white/10')
    content = content.replace('border-white/5', 'border-zinc-200 dark:border-white/5')
    content = content.replace('bg-white/5 ', 'bg-zinc-100 dark:bg-white/5 ')
    content = content.replace('bg-white/5"', 'bg-zinc-100 dark:bg-white/5"')
    content = content.replace('text-zinc-400', 'text-zinc-500 dark:text-zinc-400')
    content = content.replace('hover:bg-white/5', 'hover:bg-zinc-100 dark:hover:bg-white/5')
    content = content.replace('hover:text-white', 'hover:text-zinc-900 dark:hover:text-white')
    content = content.replace('bg-zinc-900/50', 'bg-white dark:bg-zinc-900/50')
    content = content.replace('bg-zinc-900/30', 'bg-zinc-100 dark:bg-zinc-900/30')
    # Use re.sub with word boundaries for exact class matches
    content = re.sub(r'\bbg-zinc-900\b', 'bg-white dark:bg-zinc-900', content)
    content = content.replace('hover:bg-zinc-800', 'hover:bg-zinc-100 dark:hover:bg-zinc-800')
    content = content.replace('bg-zinc-800/50', 'bg-zinc-200 dark:bg-zinc-800/50')
    content = content.replace('text-zinc-700', 'text-zinc-400 dark:text-zinc-700')
    content = re.sub(r'\btext-zinc-500\b', 'text-zinc-500 dark:text-zinc-400', content)
    content = re.sub(r'\btext-zinc-600\b', 'text-zinc-500 dark:text-zinc-600', content)
    
    # Finally fix any remaining loose text-white instances EXCEPT those in border-white/xx or bg-white/xx or dark:text-white
    # It's safer to just let the main container handle text color (text-zinc-900 dark:text-white) and only replace explicit ones if needed.
    return content

for file_path in directories:
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
            new_content = apply_replacements(content)
        with open(file_path, 'w') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
