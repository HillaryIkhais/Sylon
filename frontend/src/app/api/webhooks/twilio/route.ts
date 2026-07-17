import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  try {
    const formData = await request.formData();
    const payload = Object.fromEntries(formData.entries());
    
    // Log for debugging
    console.log('[Next.js Gateway] Received Twilio Webhook Payload:', JSON.stringify(payload, null, 2));

    // Forward the payload to the Python AI Microservice asynchronously
    const pythonBackendUrl = process.env.PYTHON_BACKEND_URL || 'https://morlen.onrender.com';
    
    fetch(`${pythonBackendUrl}/webhooks/twilio/internal/process-twilio`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    }).catch(err => {
      console.error('[Next.js Gateway] Failed to forward payload to Python:', err);
    });

    // Twilio expects a valid XML TwiML response, but since we are handling this via 
    // a separate async thread, returning an empty 200 OK is sufficient to ack the webhook.
    return new NextResponse('<?xml version="1.0" encoding="UTF-8"?><Response></Response>', {
      status: 200,
      headers: {
        'Content-Type': 'text/xml',
      },
    });
  } catch (error) {
    console.error('[Next.js Gateway] Webhook processing error:', error);
    return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
  }
}
