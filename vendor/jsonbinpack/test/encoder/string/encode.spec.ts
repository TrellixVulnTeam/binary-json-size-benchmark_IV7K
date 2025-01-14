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
  STRING_DICTIONARY_COMPRESSOR,
  STRING_BROTLI,
  URL_PROTOCOL_HOST_REST,
  RFC3339_DATE_INTEGER_TRIPLET,
  BOUNDED_PREFIX_LENGTH_8BIT_FIXED,
  ROOF_PREFIX_LENGTH_ENUM_VARINT,
  UTF8_STRING_NO_LENGTH,
  SHARED_STRING_POINTER_RELATIVE_OFFSET,
  FLOOR_PREFIX_LENGTH_ENUM_VARINT,
  STRING_UNBOUNDED_SCOPED_PREFIX_LENGTH
} from '../../../lib/encoder/string/encode'

import {
  BoundedOptions,
  RoofOptions,
  FloorOptions
} from '../../../lib/encoder/string/options'

import {
  ResizableBuffer,
  EncodingContext,
  getDefaultEncodingContext
} from '../../../lib/encoder'

tap.test('STRING_DICTIONARY_COMPRESSOR: should encode "" with [ bar ]', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(1))
  const bytesWritten: number =
    STRING_DICTIONARY_COMPRESSOR(buffer, 0, '', {
      index: [ 'bar' ],
      dictionary: {
        bar: 0
      }
    }, context)

  test.strictSame(buffer.getBuffer(), Buffer.from([ 0x00 ]))
  test.is(bytesWritten, 1)
  test.end()
})

tap.test('STRING_DICTIONARY_COMPRESSOR: should encode "foo bar baz" with [ bar ]', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(10))
  const bytesWritten: number =
    STRING_DICTIONARY_COMPRESSOR(buffer, 0, 'foo bar baz', {
      index: [ 'bar' ],
      dictionary: {
        bar: 0
      }
    }, context)

  test.strictSame(buffer.getBuffer(), Buffer.from([
    // Whole string length
    0x0b,

    // Zigzag negative length + 'foo'
    0x07, 0x66, 0x6f, 0x6f,

    // 'bar'
    0x02,

    // Zigzag negative length + 'baz'
    0x07, 0x62, 0x61, 0x7a
  ]))

  test.is(bytesWritten, 10)
  test.end()
})

tap.test('STRING_DICTIONARY_COMPRESSOR: should encode "foo bar foo" with [ bar ]', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(11))
  const bytesWritten: number =
    STRING_DICTIONARY_COMPRESSOR(buffer, 0, 'foo bar foo', {
      index: [ 'bar' ],
      dictionary: {
        bar: 0
      }
    }, context)

  test.strictSame(buffer.getBuffer(), Buffer.from([
    // Whole string length
    0x0b,

    // Zigzag negative length + 'foo'
    0x07, 0x66, 0x6f, 0x6f,

    // 'bar'
    0x02,

    // Start of shared string
    0x00,

    // Zigzag negative length + offset 'foo'
    0x03, 0x06
  ]))

  test.is(bytesWritten, 9)
  test.end()
})

tap.test('STRING_DICTIONARY_COMPRESSOR: should encode "bar foo foo" with [ bar ]', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(10))
  const bytesWritten: number =
    STRING_DICTIONARY_COMPRESSOR(buffer, 0, 'bar foo foo', {
      index: [ 'bar' ],
      dictionary: {
        bar: 0
      }
    }, context)

  test.strictSame(buffer.getBuffer(), Buffer.from([
    // Whole string length
    0x0b,

    // 'bar'
    0x02,

    // Zigzag negative length
    0x0f,

    // 'foo foo'
    0x66, 0x6f, 0x6f, 0x20, 0x66, 0x6f, 0x6f
  ]))

  test.is(bytesWritten, 10)
  test.end()
})

tap.test('STRING_BROTLI: should encode "foo bar baz"', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(16))
  const bytesWritten: number = STRING_BROTLI(buffer, 0, 'foo bar baz', {}, context)
  test.strictSame(buffer.getBuffer(), Buffer.from([
    0x0f, 0x0b, 0x05, 0x80, 0x66, 0x6f, 0x6f, 0x20,
    0x62, 0x61, 0x72, 0x20, 0x62, 0x61, 0x7a, 0x03
  ]))
  test.is(bytesWritten, 16)
  test.end()
})

tap.test('URL_PROTOCOL_HOST_REST: should encode "https://google.com"', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(18))
  const bytesWritten: number =
    URL_PROTOCOL_HOST_REST(buffer, 0, 'https://google.com', {}, context)
  test.strictSame(buffer.getBuffer(), Buffer.from([
    // Protocol length
    0x06,

    // 'https'
    0x68, 0x74, 0x74, 0x70, 0x73,

    // Host length
    0x0b,

    // 'google.com'
    0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x63, 0x6f, 0x6d,

    // Rest length
    0x01
  ]))
  test.is(bytesWritten, 18)
  test.end()
})

tap.test('URL_PROTOCOL_HOST_REST: should encode "https://google.com/"', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(19))
  const bytesWritten: number =
    URL_PROTOCOL_HOST_REST(buffer, 0, 'https://google.com/', {}, context)
  test.strictSame(buffer.getBuffer(), Buffer.from([
    // Protocol length
    0x06,

    // 'https'
    0x68, 0x74, 0x74, 0x70, 0x73,

    // Host length
    0x0b,

    // 'google.com'
    0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x63, 0x6f, 0x6d,

    // Rest length
    0x02,
    0x2f
  ]))
  test.is(bytesWritten, 19)
  test.end()
})

tap.test('URL_PROTOCOL_HOST_REST: should encode "https://google.com/foo"', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(22))
  const bytesWritten: number =
    URL_PROTOCOL_HOST_REST(buffer, 0, 'https://google.com/foo', {}, context)
  test.strictSame(buffer.getBuffer(), Buffer.from([
    // Protocol length
    0x06,

    // 'https'
    0x68, 0x74, 0x74, 0x70, 0x73,

    // Host length
    0x0b,

    // 'google.com'
    0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x63, 0x6f, 0x6d,

    // Rest length
    0x05,
    0x2f, 0x66, 0x6f, 0x6f
  ]))
  test.is(bytesWritten, 22)
  test.end()
})

tap.test('URL_PROTOCOL_HOST_REST: should encode "https://google.com/foo?bar=1"', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(28))
  const bytesWritten: number =
    URL_PROTOCOL_HOST_REST(buffer, 0, 'https://google.com/foo?bar=1', {}, context)
  test.strictSame(buffer.getBuffer(), Buffer.from([
    // Protocol length
    0x06,

    // 'https'
    0x68, 0x74, 0x74, 0x70, 0x73,

    // Host length
    0x0b,

    // 'google.com'
    0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x63, 0x6f, 0x6d,

    // Rest length
    0x0b,
    0x2f, 0x66, 0x6f, 0x6f,

    // Query string
    0x3f, 0x62, 0x61, 0x72, 0x3d, 0x31
  ]))
  test.is(bytesWritten, 28)
  test.end()
})

tap.test('RFC3339_DATE_INTEGER_TRIPLET: should encode "2014-10-01"', (test) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(4))
  const bytesWritten: number =
    RFC3339_DATE_INTEGER_TRIPLET(buffer, 0, '2014-10-01', {}, context)
  test.strictSame(buffer.getBuffer(), Buffer.from([ 0xde, 0x07, 0x0a, 0x01 ]))
  test.is(bytesWritten, 4)
  test.end()
})

tap.test('ROOF_PREFIX_LENGTH_ENUM_VARINT: should encode "foo" (..4)', (
  test
) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(4))
  const bytesWritten: number =
    ROOF_PREFIX_LENGTH_ENUM_VARINT(buffer, 0, 'foo', {
      maximum: 4
    }, context)
  test.strictSame(buffer.getBuffer(), Buffer.from([ 0x02, 0x66, 0x6f, 0x6f ]))
  test.is(bytesWritten, 4)
  test.end()
})

tap.test('ROOF_PREFIX_LENGTH_ENUM_VARINT: should encode "fooo" (..4)', (
  test
) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(4))
  const bytesWritten: number =
    ROOF_PREFIX_LENGTH_ENUM_VARINT(buffer, 0, 'fooo', {
      maximum: 4
    }, context)
  test.strictSame(buffer.getBuffer(), Buffer.from([ 0x01, 0x66, 0x6f, 0x6f, 0x6f ]))
  test.is(bytesWritten, 5)
  test.end()
})

tap.test('FLOOR_PREFIX_LENGTH_ENUM_VARINT: should encode "foo" (3..)', (
  test
) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(4))
  const bytesWritten: number =
    FLOOR_PREFIX_LENGTH_ENUM_VARINT(buffer, 0, 'foo', {
      minimum: 3
    }, context)
  test.strictSame(buffer.getBuffer(), Buffer.from([ 0x01, 0x66, 0x6f, 0x6f ]))
  test.is(bytesWritten, 4)
  test.end()
})

tap.test('BOUNDED_PREFIX_LENGTH_8BIT_FIXED: should encode a shared string', (
  test
) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(10))
  const options: BoundedOptions = {
    minimum: 0,
    maximum: 4
  }

  const bytesWritten1: number = BOUNDED_PREFIX_LENGTH_8BIT_FIXED(
    buffer, 0, 'foo', options, context)

  const bytesWritten2: number = BOUNDED_PREFIX_LENGTH_8BIT_FIXED(
    buffer, bytesWritten1, 'foo', options, context)

  test.strictSame(buffer.getBuffer(), Buffer.from([
    // String length + foo
    0x04, 0x66, 0x6f, 0x6f,

    // Start of pointer
    0x00,

    // String length
    0x04,

    // Pointer (current = 6 - location = 1)
    0x05
  ]))

  test.is(context.strings.get('foo'), 1)
  test.false(context.keys.has('foo'))
  test.is(bytesWritten1, 4)
  test.is(bytesWritten2, 3)

  test.end()
})

tap.test('ROOF_PREFIX_LENGTH_ENUM_VARINT: should encode a shared string', (
  test
) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(10))
  const options: RoofOptions = {
    maximum: 4
  }

  const bytesWritten1: number = ROOF_PREFIX_LENGTH_ENUM_VARINT(
    buffer, 0, 'foo', options, context)

  const bytesWritten2: number = ROOF_PREFIX_LENGTH_ENUM_VARINT(
    buffer, bytesWritten1, 'foo', options, context)

  test.strictSame(buffer.getBuffer(), Buffer.from([
    // String length + foo
    0x02, 0x66, 0x6f, 0x6f,

    // Start of pointer
    0x00,

    // String length
    0x02,

    // Pointer (current = 6 - location = 1)
    0x05
  ]))

  test.is(context.strings.get('foo'), 1)
  test.false(context.keys.has('foo'))
  test.is(bytesWritten1, 4)
  test.is(bytesWritten2, 3)

  test.end()
})

tap.test('UTF8_STRING_NO_LENGTH: should encode a string', (
  test
) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(3))
  const bytesWritten: number = UTF8_STRING_NO_LENGTH(
    buffer, 0, 'foo', {
      size: 3
    }, context)

  test.strictSame(buffer.getBuffer(), Buffer.from([
    // 'foo'
    0x66, 0x6f, 0x6f
  ]))

  test.is(context.strings.get('foo'), 0)
  test.false(context.keys.has('foo'))
  test.is(bytesWritten, 3)
  test.end()
})

tap.test('SHARED_STRING_POINTER_RELATIVE_OFFSET: should encode a shared string', (
  test
) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(4))

  const bytesWritten1: number = UTF8_STRING_NO_LENGTH(
    buffer, 0, 'foo', {
      size: 3
    }, context)
  const bytesWritten2: number = SHARED_STRING_POINTER_RELATIVE_OFFSET(
    buffer, bytesWritten1, 'foo', {
      size: 3
    }, context)

  test.strictSame(buffer.getBuffer(), Buffer.from([
    // 'foo'
    0x66, 0x6f, 0x6f,

    // Offset
    0x03
  ]))

  test.is(context.strings.get('foo'), 0)
  test.false(context.keys.has('foo'))
  test.is(bytesWritten1, 3)
  test.is(bytesWritten2, 1)
  test.end()
})

tap.test('FLOOR_PREFIX_LENGTH_ENUM_VARINT: should encode a shared string', (
  test
) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(10))
  const options: FloorOptions = {
    minimum: 3
  }

  const bytesWritten1: number = FLOOR_PREFIX_LENGTH_ENUM_VARINT(
    buffer, 0, 'foo', options, context)

  const bytesWritten2: number = FLOOR_PREFIX_LENGTH_ENUM_VARINT(
    buffer, bytesWritten1, 'foo', options, context)

  test.strictSame(buffer.getBuffer(), Buffer.from([
    // String length + foo
    0x01, 0x66, 0x6f, 0x6f,

    // Start of pointer
    0x00,

    // String length
    0x01,

    // Pointer (current = 6 - location = 1)
    0x05
  ]))

  test.is(context.strings.get('foo'), 1)
  test.false(context.keys.has('foo'))
  test.is(bytesWritten1, 4)
  test.is(bytesWritten2, 3)

  test.end()
})

tap.test('STRING_UNBOUNDED_SCOPED_PREFIX_LENGTH: should encode "foo"', (
  test
) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(4))
  const bytesWritten: number =
    STRING_UNBOUNDED_SCOPED_PREFIX_LENGTH(buffer, 0, 'foo', {}, context)
  test.strictSame(buffer.getBuffer(), Buffer.from([ 0x04, 0x66, 0x6f, 0x6f ]))
  test.is(bytesWritten, 4)
  test.end()
})

tap.test('STRING_UNBOUNDED_SCOPED_PREFIX_LENGTH: should encode a shared string', (
  test
) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(10))

  const bytesWritten1: number = STRING_UNBOUNDED_SCOPED_PREFIX_LENGTH(
    buffer, 0, 'foo', {}, context)

  const bytesWritten2: number = STRING_UNBOUNDED_SCOPED_PREFIX_LENGTH(
    buffer, bytesWritten1, 'foo', {}, context)

  test.strictSame(buffer.getBuffer(), Buffer.from([
    // String length + foo
    0x04, 0x66, 0x6f, 0x6f,

    // Start of pointer
    0x00,

    // Pointer (current = 5 - location = 0)
    0x05
  ]))

  test.is(context.strings.get('foo'), 1)
  test.is(context.keys.get('foo'), 4)
  test.is(bytesWritten1, 4)
  test.is(bytesWritten2, 2)

  test.end()
})

tap.test('STRING_UNBOUNDED_SCOPED_PREFIX_LENGTH: should not encode a shared non-key string', (
  test
) => {
  const context: EncodingContext = getDefaultEncodingContext()
  const buffer: ResizableBuffer = new ResizableBuffer(Buffer.allocUnsafe(10))

  const bytesWritten1: number = FLOOR_PREFIX_LENGTH_ENUM_VARINT(
    buffer, 0, 'foo', {
      minimum: 3
    }, context)

  const bytesWritten2: number = STRING_UNBOUNDED_SCOPED_PREFIX_LENGTH(
    buffer, bytesWritten1, 'foo', {}, context)

  test.strictSame(buffer.getBuffer(), Buffer.from([
    // String length + foo
    0x01, 0x66, 0x6f, 0x6f,

    // String length + foo
    0x04, 0x66, 0x6f, 0x6f
  ]))

  test.is(context.strings.get('foo'), 5)
  test.is(context.keys.get('foo'), 4)
  test.is(bytesWritten1, 4)
  test.is(bytesWritten2, 4)

  test.end()
})
