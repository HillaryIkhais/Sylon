import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  try {
    const payload = await request.json();
    
    // Log for debugging
    console.log('[Next.js Gateway] Received Bird Webhook Payload:', JSON.stringify(payload, null, 2));

    // Forward the payload to the Python AI Microservice asynchronously
    const pythonBackendUrl = process.env.PYTHON_BACKEND_URL || 'http://127.0.0.1:8000';
    
    fetch(`${pythonBackendUrl}/webhooks/bird/internal/process-bird`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    }).catch(err => {
      console.error('[Next.js Gateway] Failed to forward payload to Python:', err);
    });

    // Instantly acknowledge receipt
    return NextResponse.json({ status: 'ok' }, { status: 200 });
  } catch (error) {
    console.error('[Next.js Gateway] Webhook processing error:', error);
    return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
  }
}
