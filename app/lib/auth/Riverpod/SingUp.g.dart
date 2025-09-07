// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'SingUp.dart';

// **************************************************************************
// RiverpodGenerator
// **************************************************************************

@ProviderFor(Singup)
const singupProvider = SingupProvider._();

final class SingupProvider
    extends $NotifierProvider<Singup, AsyncValue<UserModel>> {
  const SingupProvider._()
    : super(
        from: null,
        argument: null,
        retry: null,
        name: r'singupProvider',
        isAutoDispose: true,
        dependencies: null,
        $allTransitiveDependencies: null,
      );

  @override
  String debugGetCreateSourceHash() => _$singupHash();

  @$internal
  @override
  Singup create() => Singup();

  /// {@macro riverpod.override_with_value}
  Override overrideWithValue(AsyncValue<UserModel> value) {
    return $ProviderOverride(
      origin: this,
      providerOverride: $SyncValueProvider<AsyncValue<UserModel>>(value),
    );
  }
}

String _$singupHash() => r'0c8c9c8fe0bfbcc412c8cfe50c29b17784c4b40c';

abstract class _$Singup extends $Notifier<AsyncValue<UserModel>> {
  AsyncValue<UserModel> build();
  @$mustCallSuper
  @override
  void runBuild() {
    final created = build();
    final ref = this.ref as $Ref<AsyncValue<UserModel>, AsyncValue<UserModel>>;
    final element =
        ref.element
            as $ClassProviderElement<
              AnyNotifier<AsyncValue<UserModel>, AsyncValue<UserModel>>,
              AsyncValue<UserModel>,
              Object?,
              Object?
            >;
    element.handleValue(ref, created);
  }
}

// ignore_for_file: type=lint
// ignore_for_file: subtype_of_sealed_class, invalid_use_of_internal_member, invalid_use_of_visible_for_testing_member, deprecated_member_use_from_same_package
