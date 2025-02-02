"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.URL_PROTOCOL_HOST_REST = exports.STRING_UNBOUNDED_SCOPED_PREFIX_LENGTH = exports.FLOOR_PREFIX_LENGTH_ENUM_VARINT = exports.SHARED_STRING_POINTER_RELATIVE_OFFSET = exports.UTF8_STRING_NO_LENGTH = exports.ROOF_PREFIX_LENGTH_ENUM_VARINT = exports.BOUNDED_PREFIX_LENGTH_8BIT_FIXED = exports.RFC3339_DATE_INTEGER_TRIPLET = exports.STRING_DICTIONARY_COMPRESSOR = exports.STRING_BROTLI = void 0;
var assert_1 = require("assert");
var zlib_1 = require("zlib");
var decode_1 = require("../integer/decode");
var limits_1 = require("../../utils/limits");
var types_1 = require("../any/types");
var STRING_ENCODING = 'utf8';
var readSharedString = function (buffer, offset, prefix, length, delta) {
    var pointerOffset = offset + prefix.bytes + length.bytes;
    var pointer = decode_1.FLOOR_ENUM_VARINT(buffer, pointerOffset, {
        minimum: 0
    });
    var stringOffset = pointerOffset - pointer.value;
    return {
        value: buffer.toString(STRING_ENCODING, stringOffset, stringOffset + length.value + delta),
        bytes: prefix.bytes + length.bytes + pointer.bytes
    };
};
var STRING_BROTLI = function (buffer, offset, _options) {
    var length = decode_1.FLOOR_ENUM_VARINT(buffer, offset, {
        minimum: 0
    });
    var slice = buffer.slice(offset + length.bytes, offset + length.bytes + length.value);
    return {
        value: zlib_1.brotliDecompressSync(slice).toString(STRING_ENCODING),
        bytes: length.bytes + length.value
    };
};
exports.STRING_BROTLI = STRING_BROTLI;
var STRING_DICTIONARY_COMPRESSOR = function (buffer, offset, options) {
    var length = decode_1.FLOOR_ENUM_VARINT(buffer, offset, {
        minimum: 0
    });
    var cursor = offset + length.bytes;
    var result = '';
    while (Buffer.byteLength(result, STRING_ENCODING) < length.value) {
        var prefix = result.length === 0 ? '' : ' ';
        var markerResult = decode_1.ARBITRARY_ZIGZAG_VARINT(buffer, cursor, {});
        cursor += markerResult.bytes;
        if (markerResult.value > 0) {
            var fragment = options.index[markerResult.value - 1];
            assert_1.strict(typeof fragment === 'string');
            result += prefix + fragment;
        }
        else if (markerResult.value < 0) {
            var fragmentLength = -markerResult.value - 1;
            assert_1.strict(fragmentLength >= 0);
            var fragment = buffer.toString(STRING_ENCODING, cursor, cursor + fragmentLength);
            result += prefix + fragment;
            cursor += fragmentLength;
        }
        else {
            var lengthMarker = decode_1.FLOOR_ENUM_VARINT(buffer, cursor, {
                minimum: 0
            });
            var fragment = readSharedString(buffer, cursor - markerResult.bytes, markerResult, lengthMarker, 0);
            result += prefix + fragment.value;
            cursor += fragment.bytes - 1;
        }
    }
    return {
        value: result,
        bytes: cursor - offset
    };
};
exports.STRING_DICTIONARY_COMPRESSOR = STRING_DICTIONARY_COMPRESSOR;
var RFC3339_DATE_INTEGER_TRIPLET = function (buffer, offset, _options) {
    var year = buffer.readUInt16LE(offset);
    var month = buffer.readUInt8(offset + 2);
    var day = buffer.readUInt8(offset + 3);
    assert_1.strict(year <= 9999);
    assert_1.strict(month >= 1 && month <= 12);
    assert_1.strict(day >= 1 && day <= 31);
    var yearString = String(year).padStart(4, '0');
    var monthString = String(month).padStart(2, '0');
    var dayString = String(day).padStart(2, '0');
    return {
        value: yearString + "-" + monthString + "-" + dayString,
        bytes: 4
    };
};
exports.RFC3339_DATE_INTEGER_TRIPLET = RFC3339_DATE_INTEGER_TRIPLET;
var BOUNDED_PREFIX_LENGTH_8BIT_FIXED = function (buffer, offset, options) {
    assert_1.strict(options.minimum >= 0);
    assert_1.strict(options.maximum >= options.minimum);
    assert_1.strict(options.maximum - options.minimum <= limits_1.UINT8_MAX);
    var prefix = decode_1.BOUNDED_8BITS_ENUM_FIXED(buffer, offset, {
        minimum: options.minimum,
        maximum: options.maximum + 1
    });
    if (prefix.value === types_1.Type.SharedString) {
        var length_1 = decode_1.BOUNDED_8BITS_ENUM_FIXED(buffer, offset + prefix.bytes, {
            minimum: options.minimum,
            maximum: options.maximum + 1
        });
        return readSharedString(buffer, offset, prefix, length_1, -1);
    }
    return {
        value: buffer.toString(STRING_ENCODING, offset + prefix.bytes, offset + prefix.bytes + prefix.value - 1),
        bytes: prefix.bytes + prefix.value - 1
    };
};
exports.BOUNDED_PREFIX_LENGTH_8BIT_FIXED = BOUNDED_PREFIX_LENGTH_8BIT_FIXED;
var ROOF_PREFIX_LENGTH_ENUM_VARINT = function (buffer, offset, options) {
    assert_1.strict(options.maximum >= 0);
    var prefix = decode_1.ROOF_MIRROR_ENUM_VARINT(buffer, offset, options);
    if (prefix.value === options.maximum) {
        var length_2 = decode_1.ROOF_MIRROR_ENUM_VARINT(buffer, offset + prefix.bytes, options);
        return readSharedString(buffer, offset, prefix, length_2, 1);
    }
    return {
        value: buffer.toString(STRING_ENCODING, offset + prefix.bytes, offset + prefix.bytes + prefix.value + 1),
        bytes: prefix.bytes + prefix.value + 1
    };
};
exports.ROOF_PREFIX_LENGTH_ENUM_VARINT = ROOF_PREFIX_LENGTH_ENUM_VARINT;
var UTF8_STRING_NO_LENGTH = function (buffer, offset, options) {
    assert_1.strict(options.size >= 0);
    return {
        value: buffer.toString(STRING_ENCODING, offset, offset + options.size),
        bytes: options.size
    };
};
exports.UTF8_STRING_NO_LENGTH = UTF8_STRING_NO_LENGTH;
var SHARED_STRING_POINTER_RELATIVE_OFFSET = function (buffer, offset, options) {
    return readSharedString(buffer, offset, {
        value: 0,
        bytes: 0
    }, {
        value: options.size,
        bytes: 0
    }, 0);
};
exports.SHARED_STRING_POINTER_RELATIVE_OFFSET = SHARED_STRING_POINTER_RELATIVE_OFFSET;
var FLOOR_PREFIX_LENGTH_ENUM_VARINT = function (buffer, offset, options) {
    assert_1.strict(options.minimum >= 0);
    var prefix = decode_1.FLOOR_ENUM_VARINT(buffer, offset, options);
    if (prefix.value === options.minimum) {
        var length_3 = decode_1.FLOOR_ENUM_VARINT(buffer, offset + prefix.bytes, options);
        return readSharedString(buffer, offset, prefix, length_3, -1);
    }
    var result = exports.UTF8_STRING_NO_LENGTH(buffer, offset + prefix.bytes, {
        size: prefix.value - 1
    });
    return {
        value: result.value,
        bytes: result.bytes + prefix.bytes
    };
};
exports.FLOOR_PREFIX_LENGTH_ENUM_VARINT = FLOOR_PREFIX_LENGTH_ENUM_VARINT;
var STRING_UNBOUNDED_SCOPED_PREFIX_LENGTH = function (buffer, offset, options) {
    var prefix = decode_1.FLOOR_ENUM_VARINT(buffer, offset, {
        minimum: 0
    });
    if (prefix.value === 0) {
        var pointer = decode_1.FLOOR_ENUM_VARINT(buffer, offset + prefix.bytes, {
            minimum: 0
        });
        var cursor = offset + prefix.bytes - pointer.value;
        var length_4 = decode_1.FLOOR_ENUM_VARINT(buffer, cursor, {
            minimum: 0
        });
        if (length_4.value === 0) {
            var result_1 = exports.STRING_UNBOUNDED_SCOPED_PREFIX_LENGTH(buffer, cursor, options);
            return {
                value: result_1.value,
                bytes: prefix.bytes + pointer.bytes
            };
        }
        var result_2 = exports.UTF8_STRING_NO_LENGTH(buffer, cursor + length_4.bytes, {
            size: length_4.value - 1
        });
        return {
            value: result_2.value,
            bytes: prefix.bytes + pointer.bytes
        };
    }
    var result = exports.UTF8_STRING_NO_LENGTH(buffer, offset + prefix.bytes, {
        size: prefix.value - 1
    });
    return {
        value: result.value,
        bytes: result.bytes + prefix.bytes
    };
};
exports.STRING_UNBOUNDED_SCOPED_PREFIX_LENGTH = STRING_UNBOUNDED_SCOPED_PREFIX_LENGTH;
var URL_PROTOCOL_HOST_REST = function (buffer, offset, _options) {
    var protocol = exports.FLOOR_PREFIX_LENGTH_ENUM_VARINT(buffer, offset, {
        minimum: 0
    });
    var host = exports.FLOOR_PREFIX_LENGTH_ENUM_VARINT(buffer, offset + protocol.bytes, {
        minimum: 0
    });
    var rest = exports.FLOOR_PREFIX_LENGTH_ENUM_VARINT(buffer, offset + protocol.bytes + host.bytes, {
        minimum: 0
    });
    return {
        value: protocol.value + "://" + host.value + rest.value,
        bytes: protocol.bytes + host.bytes + rest.bytes
    };
};
exports.URL_PROTOCOL_HOST_REST = URL_PROTOCOL_HOST_REST;
