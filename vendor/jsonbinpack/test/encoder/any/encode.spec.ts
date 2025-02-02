/*
 * Copyright 2021 Juan Cruz Viotti
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import tap from 'tap'

import {
  ANY_PACKED_TYPE_TAG_BYTE_PREFIX
} from '../../../lib/encoder/any/encode'

import {
  ResizableBuffer,
  EncodingContext,
  getDefaultEncodingContext
} from '../../../lib/encoder'

tap.test('ANY_PACKED_TYPE_TAG_BYTE_PREFIX: should encode null as 0x17', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(1))
  const bytesWritten: number = ANY_PACKED_TYPE_TAG_BYTE_PREFIX(buffer, 0, null, {}, context)
  test.strictSame(buffer.getBuffer(), Buffer.from([ 0x17 ]))
  test.is(bytesWritten, 1)
  test.end()
})

tap.test('ANY_PACKED_TYPE_TAG_BYTE_PREFIX: should encode false as 0x07', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(1))
  const bytesWritten: number = ANY_PACKED_TYPE_TAG_BYTE_PREFIX(buffer, 0, false, {}, context)
  test.strictSame(buffer.getBuffer(), Buffer.from([ 0x07 ]))
  test.is(bytesWritten, 1)
  test.end()
})

tap.test('ANY_PACKED_TYPE_TAG_BYTE_PREFIX: should encode true as 0x0f', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(1))
  const bytesWritten: number = ANY_PACKED_TYPE_TAG_BYTE_PREFIX(buffer, 0, true, {}, context)
  test.strictSame(buffer.getBuffer(), Buffer.from([ 0x0f ]))
  test.is(bytesWritten, 1)
  test.end()
})

tap.test('ANY_PACKED_TYPE_TAG_BYTE_PREFIX: should encode "foo" as 0x21 + string', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(4))
  const bytesWritten: number = ANY_PACKED_TYPE_TAG_BYTE_PREFIX(buffer, 0, 'foo', {}, context)
  test.strictSame(buffer.getBuffer(), Buffer.from([ 0x21, 0x66, 0x6f, 0x6f ]))
  test.is(bytesWritten, 4)
  test.end()
})

tap.test('ANY_PACKED_TYPE_TAG_BYTE_PREFIX: should encode "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" (30)', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(31))
  const value: string = 'x'.repeat(30)
  const bytesWritten: number = ANY_PACKED_TYPE_TAG_BYTE_PREFIX(buffer, 0, value, {}, context)
  test.strictSame(buffer.getBuffer(), Buffer.from([
    0xf9,
    0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78,
    0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78,
    0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78
  ]))

  test.is(bytesWritten, 31)
  test.end()
})

tap.test('ANY_PACKED_TYPE_TAG_BYTE_PREFIX: should encode "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" (31)', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(32))
  const value: string = 'x'.repeat(31)
  const bytesWritten: number = ANY_PACKED_TYPE_TAG_BYTE_PREFIX(buffer, 0, value, {}, context)
  test.strictSame(buffer.getBuffer(), Buffer.from([
    0x02,
    0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78,
    0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78,
    0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78,
    0x78
  ]))

  test.is(bytesWritten, 32)
  test.end()
})

tap.test('ANY_PACKED_TYPE_TAG_BYTE_PREFIX: should encode "https://soundcloud.com/dandymusicnl"', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(36))
  const value: string = 'https://soundcloud.com/dandymusicnl'
  const bytesWritten: number = ANY_PACKED_TYPE_TAG_BYTE_PREFIX(buffer, 0, value, {}, context)
  test.strictSame(buffer.getBuffer(), Buffer.from([
    0x22,

    0x68, 0x74, 0x74, 0x70, 0x73, 0x3a, 0x2f, 0x2f, 0x73,
    0x6f, 0x75, 0x6e, 0x64, 0x63, 0x6c, 0x6f, 0x75, 0x64,
    0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6e, 0x64,
    0x79, 0x6d, 0x75, 0x73, 0x69, 0x63, 0x6e, 0x6c
  ]))

  test.is(bytesWritten, 36)
  test.end()
})

tap.test('ANY_PACKED_TYPE_TAG_BYTE_PREFIX: should encode " " as 0x11 0x20', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(2))
  const bytesWritten: number = ANY_PACKED_TYPE_TAG_BYTE_PREFIX(buffer, 0, ' ', {}, context)
  test.strictSame(buffer.getBuffer(), Buffer.from([ 0x11, 0x20 ]))
  test.is(bytesWritten, 2)
  test.end()
})

tap.test('ANY_PACKED_TYPE_TAG_BYTE_PREFIX: should encode 3.14 as 0x2e + double', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(4))
  const bytesWritten: number = ANY_PACKED_TYPE_TAG_BYTE_PREFIX(buffer, 0, 3.14, {}, context)
  test.strictSame(buffer.getBuffer(), Buffer.from([
    0x2f, 0xf4, 0x04, 0x02 ]))
  test.is(bytesWritten, 4)
  test.end()
})

tap.test('ANY_PACKED_TYPE_TAG_BYTE_PREFIX: should encode 256 as 0x1f + varint', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(3))
  const bytesWritten: number = ANY_PACKED_TYPE_TAG_BYTE_PREFIX(buffer, 0, 256, {}, context)
  test.strictSame(buffer.getBuffer(), Buffer.from([ 0x1f, 0x80, 0x02 ]))
  test.is(bytesWritten, 3)
  test.end()
})

tap.test('ANY_PACKED_TYPE_TAG_BYTE_PREFIX: should encode 255 as 0x05 0xff', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(2))
  const bytesWritten: number = ANY_PACKED_TYPE_TAG_BYTE_PREFIX(buffer, 0, 255, {}, context)
  test.strictSame(buffer.getBuffer(), Buffer.from([ 0x05, 0xff ]))
  test.is(bytesWritten, 2)
  test.end()
})

tap.test('ANY_PACKED_TYPE_TAG_BYTE_PREFIX: should encode 0 as 0x0d', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(1))
  const bytesWritten: number = ANY_PACKED_TYPE_TAG_BYTE_PREFIX(buffer, 0, 0, {}, context)
  test.strictSame(buffer.getBuffer(), Buffer.from([ 0x0d ]))
  test.is(bytesWritten, 1)
  test.end()
})

tap.test('ANY_PACKED_TYPE_TAG_BYTE_PREFIX: should encode -257 as 0x27 + 256 varint', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(3))
  const bytesWritten: number = ANY_PACKED_TYPE_TAG_BYTE_PREFIX(buffer, 0, -257, {}, context)
  test.strictSame(buffer.getBuffer(), Buffer.from([ 0x27, 0x80, 0x02 ]))
  test.is(bytesWritten, 3)
  test.end()
})

tap.test('ANY_PACKED_TYPE_TAG_BYTE_PREFIX: should encode -1 as 0x0e', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(1))
  const bytesWritten: number = ANY_PACKED_TYPE_TAG_BYTE_PREFIX(buffer, 0, -1, {}, context)
  test.strictSame(buffer.getBuffer(), Buffer.from([ 0x0e ]))
  test.is(bytesWritten, 1)
  test.end()
})

tap.test('ANY_PACKED_TYPE_TAG_BYTE_PREFIX: should encode -256 as 0x06 0xff', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(2))
  const bytesWritten: number = ANY_PACKED_TYPE_TAG_BYTE_PREFIX(buffer, 0, -256, {}, context)
  test.strictSame(buffer.getBuffer(), Buffer.from([ 0x06, 0xff ]))
  test.is(bytesWritten, 2)
  test.end()
})

tap.test('ANY_PACKED_TYPE_TAG_BYTE_PREFIX: should encode {foo:"bar",baz:1}', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(17))
  const bytesWritten: number = ANY_PACKED_TYPE_TAG_BYTE_PREFIX(buffer, 0, {
    foo: 'bar',
    baz: 1
  }, {}, context)

  test.strictSame(buffer.getBuffer(), Buffer.from([
    // (Length + 1) + Tag
    0x1b,

    // Key length + 'foo'
    0x04, 0x66, 0x6f, 0x6f,

    // String tag + length + 'bar'
    0x21, 0x62, 0x61, 0x72,

    // Key length + 'baz'
    0x04, 0x62, 0x61, 0x7a,

    // Value 1 + 1 with positive integer type tag
    0x15
  ]))

  test.is(bytesWritten, 14)
  test.end()
})

tap.test('ANY_PACKED_TYPE_TAG_BYTE_PREFIX: should encode [ "foo", true, 2000 ]', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(10))
  const bytesWritten: number = ANY_PACKED_TYPE_TAG_BYTE_PREFIX(buffer, 0, [
    'foo',
    true,
    2000
  ], {}, context)

  test.strictSame(buffer.getBuffer(), Buffer.from([
    // Length + 1 with tag
    0x24,

    // "foo"
    0x21, 0x66, 0x6f, 0x6f,

    // True
    0x0f,

    // 2000
    0x1f, 0xd0, 0x0f
  ]))

  test.is(bytesWritten, 9)
  test.end()
})
