import { NextResponse } from 'next/server';

export async function GET() {
  try {
    const apiUrl = process.env.NEXT_PUBLIC_API_URL;
    
    if (!apiUrl) {
      console.log('No NEXT_PUBLIC_API_URL defined for cron.');
      return NextResponse.json({ status: 'skipped', message: 'No API URL defined' }, { status: 200 });
    }

    // Ping the root endpoint of the FastAPI backend to keep it awake
    const response = await fetch(apiUrl);
    
    if (response.ok) {
      console.log(`Successfully pinged backend: ${apiUrl}`);
      return NextResponse.json({ status: 'success', message: 'Backend pinged successfully' }, { status: 200 });
    } else {
      console.error(`Backend ping returned status: ${response.status}`);
      return NextResponse.json({ status: 'error', message: `Backend returned ${response.status}` }, { status: response.status });
    }
  } catch (error) {
    console.error('Error pinging backend:', error);
    return NextResponse.json({ status: 'error', message: 'Failed to ping backend' }, { status: 500 });
  }
}
